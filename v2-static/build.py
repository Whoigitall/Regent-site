#!/usr/bin/env python3
"""Split the master v2 file into per-route pages with unique SEO metadata.

Input:  master.html (all views in one file — the editable source)
Output: pricing.html, about.html, technology.html, pilot.html, terms.html,
        privacy.html + a rewritten index.html — each carrying ONLY its own
        view (one H1, no duplicate content), its own title/description/
        canonical/OG, and page-appropriate JSON-LD.

Run after editing the master, commit the outputs (no build step on deploy).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
BASE = "https://regentprotocol.org"

ROUTES = {
    "home": {
        "path": "/", "file": "index.html",
        "title": "Regent Protocol — Financial authorization for AI agents",
        "desc": "Regent is the financial authorization and compliance layer for AI agents that move money: verifiable identity, spending mandates, risk controls, and tamper-evident audit evidence.",
    },
    "pricing": {
        "path": "/pricing", "file": "pricing.html",
        "title": "Pricing — Regent Protocol",
        "desc": "Usage-based pricing for verifiable agent infrastructure. Free developer tier; Growth $299/mo and Scale $999/mo add mandates, Guardian, and the Control Panel; Enterprise from $2,500/mo. No per-seat pricing.",
    },
    "about": {
        "path": "/about", "file": "about.html",
        "title": "About — Regent Protocol",
        "desc": "The team and thesis behind Regent Protocol: autonomy needs accountability — verifiable identity, enforced limits, and evidence anyone can check.",
    },
    "technology": {
        "path": "/technology", "file": "technology.html",
        "title": "Technology — Regent Protocol",
        "desc": "The architecture behind verifiable agent finance: Solana settlement programs, Celestia DA audit storage, the Guardian risk engine, and a Python SDK. Live on devnet.",
    },
    "pilot": {
        "path": "/pilot", "file": "pilot.html",
        "title": "Pilot Program — Regent Protocol",
        "desc": "A structured 14-day pilot: identity, mandates, and audit evidence in front of your agents' financial actions — with our engineers in the loop. Apply online.",
    },
    "terms": {
        "path": "/terms", "file": "terms.html",
        "title": "Terms of Use — Regent Protocol",
        "desc": "Terms of Use for the Regent Protocol website, dashboard, APIs, and related services.",
    },
    "privacy": {
        "path": "/privacy", "file": "privacy.html",
        "title": "Privacy Policy — Regent Protocol",
        "desc": "How Regent Protocol collects, uses, and safeguards personal data across the website and services.",
    },
    "platform": {"path": "/platform", "file": "platform.html",
        "title": "Platform — Regent Protocol",
        "desc": "The complete system: AgentID, Mandates, Guardian, Audit Chain, and the Control Panel — one decision path for AI agents that move money."},
    "agent-id": {"path": "/platform/agent-id", "file": "platform-agent-id.html",
        "title": "AgentID — Regent Protocol",
        "desc": "A verifiable identity for every agent, connected to a responsible party — KMS-signed, DID-addressed, anchored on Solana devnet."},
    "mandates-page": {"path": "/platform/mandates", "file": "platform-mandates.html",
        "title": "Mandates — Regent Protocol",
        "desc": "Programmable spending rules enforced before execution: amounts, destinations, time windows, approvals, per-entity budgets. Try the simulator."},
    "guardian": {"path": "/platform/guardian", "file": "platform-guardian.html",
        "title": "Guardian — Regent Protocol",
        "desc": "Rule and behavioural risk signals on every action: allow, hold for a human, or stop — inside the authorization path."},
    "audit-chain": {"path": "/platform/audit-chain", "file": "platform-audit-chain.html",
        "title": "Audit Chain — Regent Protocol",
        "desc": "Tamper-evident evidence: hashes, Merkle batches, on-chain commitments — verifiable without trusting Regent or the operator."},
    "control-panel": {"path": "/platform/control-panel", "file": "platform-control-panel.html",
        "title": "Control Panel — Regent Protocol",
        "desc": "Human oversight for autonomous agents: monitoring, investigation, mandate review, and the kill switch."},
    "solutions": {"path": "/solutions", "file": "solutions.html",
        "title": "Solutions — Regent Protocol",
        "desc": "Agentic payments, fintech platforms, treasury & custody, compliance & risk — where the mandate gate and the evidence chain go to work."},
    "agentic-payments": {"path": "/solutions/agentic-payments", "file": "solutions-agentic-payments.html",
        "title": "Agentic Payments — Regent Protocol",
        "desc": "Pre-execution mandate enforcement, approval conditions, and anchored evidence for autonomous payments."},
    "fintech-platforms": {"path": "/solutions/fintech-platforms", "file": "solutions-fintech-platforms.html",
        "title": "Fintech Platforms — Regent Protocol",
        "desc": "Per-customer AgentIDs and account-scoped mandates for customer-facing agents — with a verifiable trail per customer."},
    "treasury-custody": {"path": "/solutions/treasury-custody", "file": "solutions-treasury-custody.html",
        "title": "Treasury & Custody — Regent Protocol",
        "desc": "Value, counterparty, time-window, and multi-party approval policies enforced in the execution path."},
    "compliance-risk": {"path": "/solutions/compliance-risk", "file": "solutions-compliance-risk.html",
        "title": "Compliance & Risk — Regent Protocol",
        "desc": "Case reconstruction from a single record: action, responsible context, policy, decision, evidence — independently verifiable."},
    "developers": {"path": "/developers", "file": "developers.html",
        "title": "Developers — Regent Protocol",
        "desc": "From SDK to a first verified action in one sitting: Python SDK, REST API, devnet sandbox. pip install regent."},
    "security": {"path": "/security", "file": "security.html",
        "title": "Security — Regent Protocol",
        "desc": "Security posture stated precisely: no bearer secrets on agents, fail-closed enforcement, structural tamper-evidence — and honest assurance statuses."},
    "trust": {"path": "/trust", "file": "trust.html",
        "title": "Trust Center — Regent Protocol",
        "desc": "Due-diligence statuses in one table: what runs on devnet today, what is planned, and where the evidence lives."},
}

ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization",
    "name": "Regent Protocol", "url": BASE, "logo": f"{BASE}/logo-icon.png",
    "email": "info@regentprotocol.org",
    "sameAs": [
        "https://www.linkedin.com/company/regentprotocol/",
        "https://x.com/whoigital",
        "https://www.youtube.com/@regentprotocol",
        "https://github.com/abay94/regent-platform",
    ],
}

# Offers mirror the governance rate card exactly (launch pricing).
PRICING_LD = {
    "@context": "https://schema.org", "@type": "Product",
    "name": "Regent Protocol", "description": ROUTES["pricing"]["desc"],
    "brand": {"@type": "Brand", "name": "Regent Protocol"},
    "offers": [
        {"@type": "Offer", "name": "Developer", "price": "0", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Growth", "price": "299", "priceCurrency": "USD",
         "priceSpecification": {"@type": "UnitPriceSpecification", "price": "299",
                                "priceCurrency": "USD", "billingIncrement": 1,
                                "unitText": "month"}},
        {"@type": "Offer", "name": "Scale", "price": "999", "priceCurrency": "USD",
         "priceSpecification": {"@type": "UnitPriceSpecification", "price": "999",
                                "priceCurrency": "USD", "billingIncrement": 1,
                                "unitText": "month"}},
        {"@type": "Offer", "name": "Enterprise", "price": "2500", "priceCurrency": "USD",
         "priceSpecification": {"@type": "UnitPriceSpecification", "price": "2500",
                                "priceCurrency": "USD", "billingIncrement": 1,
                                "unitText": "month"}},
    ],
}


def faq_ld(view_html: str) -> dict | None:
    """FAQPage from the VISIBLE <details class="faq"> content only (§9.2)."""
    items = []
    for m in re.finditer(r'<details class="faq">\s*<summary>(.*?)</summary>\s*<div class="a">(.*?)</div>', view_html, re.S):
        q = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        a = re.sub(r"<[^>]+>", " ", m.group(2)).strip()
        a = re.sub(r"\s+", " ", a)
        items.append({"@type": "Question", "name": q,
                      "acceptedAnswer": {"@type": "Answer", "text": a}})
    if not items:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}


def main() -> None:
    master = (HERE / "master.html").read_text()

    # locate every view block
    blocks: dict[str, str] = {}
    for name in ROUTES:
        m = re.search(rf'<div id="view-{name}"[^>]*>[\s\S]*?</div><!-- /view-{name} -->', master)
        if not m:
            sys.exit(f"view-{name} not found in master")
        blocks[name] = m.group(0)

    for name, r in ROUTES.items():
        page = master
        # keep only this view, visible
        for other, blk in blocks.items():
            if other == name:
                shown = re.sub(rf'(<div id="view-{name}")\s+hidden(>)', r"\1\2", blk)
                page = page.replace(blk, shown)
            else:
                page = page.replace(blk, "")
        # unique metadata
        page = re.sub(r"<title>.*?</title>", f"<title>{r['title']}</title>", page, count=1)
        page = re.sub(r'(<meta name="description" content=")[^"]*(">)', rf"\g<1>{r['desc']}\g<2>", page, count=1)
        page = re.sub(r'(<meta property="og:title" content=")[^"]*(">)', rf"\g<1>{r['title']}\g<2>", page, count=1)
        page = re.sub(r'(<meta property="og:description" content=")[^"]*(">)', rf"\g<1>{r['desc']}\g<2>", page, count=1)
        canonical = BASE + ("" if r["path"] == "/" else r["path"])
        head_extra = [
            f'<link rel="canonical" href="{canonical}/">' if r["path"] == "/" else f'<link rel="canonical" href="{canonical}">',
            f'<meta property="og:url" content="{canonical}">',
            f'<meta property="og:image" content="{BASE}/og-image.png">',
            '<meta property="og:type" content="website">',
        ]
        # structured data: Organization everywhere; page-specific on top
        lds = [ORG_LD]
        if name == "pricing":
            lds.append(PRICING_LD)
        if name in ("home", "pricing", "pilot", "platform"):
            ld = faq_ld(blocks[name])
            if ld:
                lds.append(ld)
        for ld in lds:
            head_extra.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
        page = page.replace("</head>", "\n".join(head_extra) + "\n</head>", 1)
        # cross-page nav: real paths (crawlable); same-page anchors stay hashes
        for other, ro in ROUTES.items():
            if other != name:
                page = page.replace(f'href="#/{other}"', f'href="{ro["path"]}"')
            else:
                page = page.replace(f'href="#/{other}"', 'href="#"')
        (HERE / r["file"]).write_text(page)
        print(f"{r['file']:16} {len(page):7} bytes  ld={len(lds)}")


if __name__ == "__main__":
    main()
