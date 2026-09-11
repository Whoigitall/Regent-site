# Copy and data for the Money20/20 Riyadh 2026 segment demo page.
# Edit here, then run: python3 build.py   (see README.md)
# Rules: no invented numbers; vocabulary matches docs.regentprotocol.org and /how-it-works;
# banned strings (KYA, Know Your Agent, DeFi, crypto, token price, yield, lending, deepfake) are scanned by build.py.

EVENT = {
    "name": "Money20/20 Riyadh 2026",
    "dates": "14–16 September",
    "stand": "Stand H2.P124 · Startup Pod",
    "badge": "Money20/20 Riyadh 2026 · 14–16 September",
}

CTA = {
    "label": "Book a 20-min meeting",
    "url": "https://wa.me/77001571111?text=Hi%20Sayat%2C%20we%20met%20at%20Money20%2F20%20Riyadh.%20Let%27s%20book%2020%20minutes.",
    "contact_line": "WhatsApp Sayat Kakzhanov, CEO: +7 700 157 1111",
    "closing": "See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh.",
    "receipt_url": "https://get4agent.com/v1/receipts/dec_5fb4e9e0e446",
    "receipt_label": "get4agent.com/v1/receipts/dec_5fb4e9e0e446",
    "site": "https://regentprotocol.org",
    "tour": "https://regentprotocol.org/how-it-works",
}

POSITIONING = {
    "kicker": "KYC verifies people. KYB verifies businesses.",
    "loud": "Regent decides what their agents may do with money, before it moves, and proves it.",
}

# Production counts pulled from the live databases on 11 September 2026 (data through 9 September 2026).
NUMBERS = {
    "as_of": "data through 9 September 2026, read on 11 September",
    "items": [
        {"n": "556", "label": "gate decisions recorded", "note": "allow, escalate or deny, each with a reason"},
        {"n": "925 / 925", "label": "audit events anchored", "note": "112 batches on Solana devnet; mainnet after program audit"},
        {"n": "67", "label": "AgentIDs issued", "note": "36 active, 31 revoked"},
        {"n": "41", "label": "active mandates", "note": "ceilings per transaction, per day, per month"},
        {"n": "12", "label": "signed receipts on get4agent.com", "note": "verifiable by anyone against our public keys"},
    ],
    "bench": "In our benchmarks (27 August 2026): authorize ~0.5 s; kill switch to first refusal 0.43–0.49 s; batch anchored ~2 s after sealing.",
}

# Shared step "learn more" texts reused across tabs
GATE_MORE = ("The trust gate checks the agent is known, its owner verified and its passport not revoked. "
             "The money gate checks amount, counterparty and expiry against the mandate. Escalate pauses for a human approval, then resumes.")
KILL_MORE = ("Guardian scores transaction patterns; above a policy threshold the gate denies or escalates. "
             "The kill switch is the owner's: every verifier that checks with Regent sees a revoked agent within seconds.")

SEGMENTS = [
    {
        "id": "banks",
        "label": "Banks & Financial Institutions",
        "short": "Banks",
        "variant": "flow",
        "org": "Bank rail",
        "promise": "Decide what an agent may do with money, before it moves.",
        "chips": [
            {"name": "Banks", "path": "allow", "packet": "invoice $180",
             "scenario": "A corporate treasury agent pays a supplier invoice. The gate checks the mandate ceiling and the approved payee list, then allows it."},
            {"name": "Neobanks", "path": "escalate", "packet": "transfer $2,400",
             "scenario": "A customer's assistant moves money between accounts. Inside the mandate it is allowed; a larger transfer escalates to the customer."},
            {"name": "Fintech & PSPs", "path": "allow", "packet": "payout $950",
             "scenario": "A merchant's agent triggers a payout. The PSP asks the gate once and receives a signed decision instead of building its own trust checks."},
            {"name": "Wallets & Card Acquiring", "path": "deny", "packet": "card $730",
             "scenario": "An agent tries a card purchase above its per-transaction ceiling. The money gate denies it before any authorisation request is sent."},
            {"name": "Insurance", "path": "allow", "packet": "premium $120",
             "scenario": "The mandate ceiling is a hard cap on what an agent can spend, and the anchored record shows every permitted and refused action. That is underwriting data."},
        ],
        "why": [
            {"icon": "wallet", "h": "Agents will move your money",
             "p": "Customers already delegate payments to assistants; the rails need a way to prove authority."},
            {"icon": "key", "h": "Authorisation is not permission",
             "p": "A signed request says who sent it, not what the agent was allowed to do."},
            {"icon": "receipt", "h": "Evidence beats dispute",
             "p": "A signed receipt turns “we think it was authorised” into a provable fact."},
        ],
        "steps": [
            {"label": "Agent arrives", "text": "An AI agent asks to act for a customer or a company.",
             "more": "The agent presents its AgentID passport. The passport proves identity only; it grants no authority by itself."},
            {"label": "Passport read", "text": "Regent resolves the AgentID and the verified owner behind it.",
             "more": "About the human, only one bit leaves Regent: verified or not. No name, no history, no reasons. A business is verified through its verified representative today; a full KYB flow is on the roadmap.", "roadmap": "KYB flow"},
            {"label": "Mandate checked", "text": "Scope, ceiling, permitted counterparties and expiry are tested against the action.",
             "more": "Limits are per transaction, per day and per month, with permitted payees and an expiry. Nothing in the key says this; the owner's approval does."},
            {"label": "The gate decides", "text": "Trust gate, then money gate: allow, escalate or deny.", "more": GATE_MORE},
            {"label": "Proof attached", "text": "A decision token and a signed receipt travel with the transaction.",
             "more": "Both are signed by Regent and checkable against our public keys, so a bank, an auditor or a counterparty can verify them without calling us."},
            {"label": "Anchored and watched", "text": "The decision is anchored; Guardian watches behaviour; the owner holds the kill switch.",
             "more": "Decisions are hashed, batched and anchored on Solana. " + KILL_MORE},
        ],
        "gives": [
            {"dim": "Revenue", "h": "Agent-ready products", "p": "Offer clients agent-initiated payments with the controls your risk teams require."},
            {"dim": "Cost", "h": "Fewer manual reviews", "p": "Verified agents clear the gate instead of being blocked wholesale."},
            {"dim": "Risk", "h": "Exposure stays inside the mandate", "p": "Unverifiable or out-of-mandate agents never reach the rail."},
            {"dim": "Speed", "h": "One decision call", "p": "A single gate replaces per-partner trust arrangements and bespoke integrations."},
        ],
        "before": "Agents are blocked, downgraded to manual review, or given static API keys that cannot express a ceiling.",
        "after": "Every agent action is tested against a live mandate and allowed, escalated or denied, with a signed receipt.",
        "subcase": {"h": "Insurance", "p": "The mandate ceiling gives an insurer a hard cap on exposure per agent, and the anchored record shows every permitted and refused action."},
        "drawer": [
            {"h": "The two gates and the three outcomes", "items": [
                "Trust gate: the agent is known, its owner verified, its passport not revoked.",
                "Money gate: amount, counterparty and expiry against the mandate.",
                "Outcomes: allow, escalate (human approval, then resume) or deny, each with a reason code.",
            ]},
            {"h": "Data objects", "items": [
                "AgentID: did:regent:solana:… bound to one verified owner.",
                "Verified-owner bit: verified or not; nothing else leaves Regent about a person.",
                "Mandate: per-transaction, per-day and per-month ceilings, permitted counterparties, currency, expiry.",
                "Decision: allow / escalate / deny, reason code, timestamp.",
                "Decision token: signed, short-lived, bound to the hash of the action.",
                "Signed receipt: the decision, verifiable against Regent's public keys at /.well-known/jwks.json.",
            ]},
            {"h": "Integration surface", "items": [
                "POST /v1/organizations/{org}/mandates/{mandate_id}/authorize returns the decision and the token.",
                "GET /v1/organizations/{org}/audit/events/{id} and POST …/verify return and check the evidence.",
                "POST /v1/organizations/{org}/agents/{agent_id}/revoke is the kill switch.",
                "Cloud Gateway: one URL and one key; every tool call gated, credentials kept in Regent's vault.",
                "Sidecar: the same gate inside your perimeter; REST API and Python SDK; MCP for agents.",
            ]},
            {"h": "How it sits next to existing controls", "items": [
                "The owner is still KYC-verified, by your provider or ours; the agent inherits that accountability.",
                "Regent extends KYC/AML to the agent's actions; it replaces nothing.",
                {"text": "KYB verification flow for business owners.", "roadmap": True},
                {"text": "Sanctions screening result as an input to the gate.", "roadmap": True},
            ]},
            {"h": "Measured in our benchmarks (27 August 2026)", "items": [
                "Authorize: about 0.5 s end to end.",
                "Kill switch to first refusal: 0.43–0.49 s.",
                "Audit batch anchored on Solana about 2 s after sealing.",
            ]},
        ],
    },
    {
        "id": "commerce",
        "label": "Commerce & Platforms",
        "short": "Commerce",
        "variant": "flow",
        "org": "Checkout",
        "promise": "Separate mandated buying agents from raw automation, and let the good ones through.",
        "chips": [
            {"name": "E-commerce", "path": "allow", "packet": "order $160",
             "scenario": "A shopping agent buys a subscription within its mandate. The gate allows it and the receipt shows the authority at purchase time."},
            {"name": "Marketplaces", "path": "allow", "packet": "listing $45",
             "scenario": "A buyer agent pays a seller through the marketplace. Every call is decided before the seller is invoked; a refusal costs nothing."},
            {"name": "Ticketing & Events", "path": "deny", "packet": "tickets $1,800",
             "scenario": "An assistant is told to buy forty tickets. The purchase ceiling denies it before the ticketing engine is asked."},
            {"name": "Rentals", "path": "escalate", "packet": "booking $980",
             "scenario": "A booking agent reserves above its daily ceiling. The gate escalates to the owner instead of failing silently."},
            {"name": "Tender & Procurement", "path": "allow", "packet": "bid",
             "scenario": "A bid agent must prove whose mandate it carries. The receipt is the evidence for procurement integrity and audit."},
        ],
        "why": [
            {"icon": "bot", "h": "Bot defences catch good agents too",
             "p": "Rules built against scraping also stop legitimate assistant-driven purchases."},
            {"icon": "traffic", "h": "Agent traffic is arriving anyway",
             "p": "The choice is between mandated agents and unmanaged automation."},
            {"icon": "ticket", "h": "Scarce inventory needs fair access",
             "p": "Ticketing, drops and tenders must weigh authority, not just volume."},
        ],
        "steps": [
            {"label": "Agent reaches your surface", "text": "A purchase, booking, bid or reservation agent arrives at your platform.",
             "more": "It signs each request with its own key and presents its AgentID passport. On get4agent.com this is live today."},
            {"label": "Passport read", "text": "Its AgentID resolves; the verified owner is a real person or business.",
             "more": "Only the verified bit about the owner leaves Regent. A business is verified through its representative today; a KYB flow is on the roadmap.", "roadmap": "KYB flow"},
            {"label": "Mandate tested", "text": "Per-purchase and per-day ceilings, permitted merchants and categories.",
             "more": "Quantity rules for scarce inventory (for example two tickets per event) and velocity thresholds are on the roadmap; today the ceiling and the merchant scope carry the policy.", "roadmap": "Quantity and velocity rules"},
            {"label": "The gate decides", "text": "Allow, escalate for a human check, or deny, before the merchant is called.",
             "more": "Same two gates as every other tab. A refusal happens before money: the merchant is never invoked and nothing is charged."},
            {"label": "Decision token attached", "text": "Approved agents check out without friction loops; the receipt is the dispute evidence.",
             "more": "Every settled call on get4agent.com carries a receipt id; anyone can verify it against Regent's public keys."},
            {"label": "Guardian and kill switch", "text": "Unusual transaction patterns are flagged; the owner can suspend the agent in seconds.",
             "more": "Guardian scores behaviour over transaction features. Named patterns such as scalping or bid manipulation are candidate rules on the roadmap. " + KILL_MORE, "roadmap": "Named abuse patterns"},
        ],
        "gives": [
            {"dim": "Revenue", "h": "An agent-ready channel", "p": "Serve assistant-driven demand that today bounces off your defences."},
            {"dim": "Cost", "h": "Less abuse handling", "p": "Mandated flows reduce fraud queues and manual dispute work."},
            {"dim": "Risk", "h": "Fewer chargebacks and scalping losses", "p": "A signed receipt shows the agent's authority at purchase time."},
            {"dim": "Speed", "h": "Less friction at checkout", "p": "Verified agents skip challenge loops; humans keep them where they matter."},
        ],
        "before": "Everything automated is treated as hostile: challenges everywhere, false declines, and scalping through the gaps.",
        "after": "Mandated agents are recognised and fast-tracked; abusive automation is identified and cut off.",
        "subcase": {"h": "Tender", "p": "A bid agent must prove whose mandate it carries, protecting procurement integrity and auditability."},
        "drawer": [
            {"h": "Decision token lifecycle", "items": [
                "Issued per allowed action, bound to the hash of that action, short-lived.",
                "The merchant or engine checks it once; the signed receipt outlives it as evidence.",
            ]},
            {"h": "The receipt as dispute evidence", "items": [
                "Fields: decision id, agent, mandate, amount and currency, outcome, timestamp, signature.",
                "Verify with any JWT library against /.well-known/jwks.json, or with the receipt verify endpoint.",
            ]},
            {"h": "Integration points", "items": [
                "Checkout or booking engine calls the gate before the payment step; the marketplace pattern is live on get4agent.com.",
                "Cloud Gateway for agents: one URL, one key; the platform runs nothing new.",
                "Bid API pattern: designed per platform during a pilot.",
            ]},
            {"h": "Guardian signals used today", "items": [
                "Amount against ceiling, decision velocity, refusal rate, time of day, counterparty novelty.",
                {"text": "Named abuse patterns (scalping, mass-hold, bid manipulation) as explicit rules.", "roadmap": True},
                {"text": "Fair-access quantity rules and velocity thresholds in the mandate.", "roadmap": True},
                {"text": "KYB verification flow for business owners.", "roadmap": True},
            ]},
        ],
    },
    {
        "id": "regulators",
        "label": "Regulators & Compliance",
        "short": "Regulators",
        "variant": "record",
        "org": "Verifier",
        "promise": "Autonomous agents, accountable to a provable decision record.",
        "chips": [
            {"name": "Central Banks & Supervisors", "focus": 5,
             "scenario": "A supervisor independently verifies receipts and the anchored audit of agents in a test environment, without trusting the platform or Regent."},
            {"name": "AML / Financial Crime", "focus": 2,
             "scenario": "Every decision names the agent, the verified-owner bit and the mandate it acted under. Screening results as a gate input are on the roadmap."},
            {"name": "Compliance & Audit", "focus": 5,
             "scenario": "An institution's compliance team queries its own decision record: who acted, under what mandate, with what outcome, and reads the receipt."},
            {"name": "Sandbox & Innovation Offices", "focus": 4,
             "scenario": "A sandbox workflow: governed agents act, the office observes decisions and revocations as they happen."},
        ],
        "why": [
            {"icon": "scale", "h": "Rules still assume human action",
             "p": "Existing frameworks do not name the agent as an accountable actor."},
            {"icon": "eye", "h": "Sampling cannot supervise agents",
             "p": "Machine-speed activity needs a queryable decision record, not monthly samples."},
            {"icon": "switch", "h": "Revocation must be fast and observable",
             "p": "A suspension is only useful if the verifiers actually see it."},
        ],
        "steps": [
            {"label": "AgentIDs are registered", "text": "Every agent governed by Regent carries a passport with a live status.",
             "more": "This is a registry of agent credentials, not of people. Status is active or revoked; nothing about the owner is listed."},
            {"label": "Decisions are recorded", "text": "Every allow, escalate or deny is anchored with its evidence.",
             "more": "The institution that made the decision can query it; the record is hashed, batched and anchored on Solana."},
            {"label": "One bit outward", "text": "About a human, only “verified” leaves Regent.",
             "more": "No reasons, no revocation history, no owner reputation and no directory of principals. Personal data stays inside the boundary."},
            {"label": "Owners can suspend", "text": "The owner or its institution suspends an agent; verifiers see it within seconds.",
             "more": "A verifier cannot revoke someone else's agent; it can stop accepting it. Revocation propagates only along paths where a verifier checks with Regent."},
            {"label": "Evidence in investigations", "text": "The record answers who authorised what, under which mandate, without reconstruction.",
             "more": "Access by authorities is a legal-basis question, not a product default. The receipt can be verified by anyone who holds it."},
            {"label": "Aggregate supervision", "text": "Market-level views and supervisory reporting are on the roadmap, not available today.",
             "more": "What exists today is per-institution querying and independently verifiable receipts.", "roadmap": "Roadmap"},
        ],
        "gives": [
            {"dim": "Revenue", "h": "Supervised growth", "p": "Licensed participation becomes defensible instead of prohibited by default."},
            {"dim": "Cost", "h": "Less manual reconstruction", "p": "Decisions arrive with their evidence attached."},
            {"dim": "Risk", "h": "Accountable agents", "p": "Every action traces to a mandate and a recorded outcome."},
            {"dim": "Speed", "h": "Read the record, do not rebuild it", "p": "Investigations read receipts and the anchored trail instead of reconstructing events."},
        ],
        "before": "Agent activity sits in a blind spot that is either banned or tolerated without evidence.",
        "after": "Each decision is provable, each agent is suspendable, and about individuals Regent still reveals only one bit.",
        "subcase": None,
        "drawer": [
            {"h": "Registry and access model", "items": [
                "Public passport resolution by DID; status active or revoked.",
                "Per-organisation audit queries with that organisation's key; no cross-organisation view.",
            ]},
            {"h": "Decision and receipt schema", "items": [
                "Decision id, agent id, mandate id, amount and currency, outcome, reason code, timestamp, signature.",
                "Public keys at /.well-known/jwks.json; receipts verifiable offline with any JWT library.",
            ]},
            {"h": "What never leaves Regent about a person", "items": [
                "One bit: verified or not. No name, no reasons, no revocation history, no reputation, no directory.",
            ]},
            {"h": "Roadmap", "items": [
                {"text": "Aggregate supervision views and supervisory export formats.", "roadmap": True},
                {"text": "Sanctions screening result as an input to the gate.", "roadmap": True},
            ]},
            {"h": "Data protection and residency", "items": [
                "The gate runs in Regent's cloud, in a dedicated instance, or inside the institution's perimeter as a sidecar.",
                "Only hashes and Merkle roots are anchored on-chain; never raw data.",
            ]},
            {"h": "How this extends AML/KYC", "items": [
                "The owner remains KYC-verified by the institution's provider or ours; the agent inherits that accountability.",
                "Nothing in the existing obligations is replaced; the agent's actions become part of the record.",
            ]},
        ],
    },
    {
        "id": "stablecoin",
        "label": "Stablecoin & tokenised settlement",
        "short": "Settlement",
        "variant": "flow",
        "org": "Settlement rail",
        "promise": "Institutional settlement where every agent is verified before value moves.",
        "chips": [
            {"name": "Stablecoin payments", "path": "allow", "packet": "transfer 1,200",
             "scenario": "An agent pays a supplier in stablecoin. The gate decides before the transfer is submitted; the receipt references the on-chain transaction."},
            {"name": "Treasury & settlement", "path": "escalate", "packet": "rebalance 50,000",
             "scenario": "A treasury agent rebalances between accounts. Amounts above the mandate ceiling escalate to the treasurer."},
            {"name": "Tokenised deposits", "path": "allow", "packet": "deposit 8,000",
             "scenario": "A bank's agent moves tokenised deposits inside the bank's rules: the same gate and the same receipt, on a bank-run ledger."},
            {"name": "Cross-border FX", "path": "deny", "packet": "FX 3,500",
             "scenario": "An agent converts and settles across borders. Permitted jurisdictions and counterparties are part of the mandate; the rest is denied."},
        ],
        "why": [
            {"icon": "key", "h": "Anonymous keys cannot pass review",
             "p": "Compliance needs to know who stands behind an agent, not just which key signed."},
            {"icon": "clock", "h": "Speed needs provable authority",
             "p": "Fast rails are only useful when authorisation can be demonstrated."},
            {"icon": "receipt", "h": "“Who authorised this?” must be answerable",
             "p": "The answer has to be recorded, not reconstructed."},
        ],
        "steps": [
            {"label": "Agent connects", "text": "The agent authenticates with its passport, not an anonymous key.",
             "more": "Each request is signed with the agent's own key (RFC 9421 HTTP message signatures); the key is bound to the AgentID."},
            {"label": "Owner verified", "text": "The entity behind the agent is confirmed; about individuals, only the verified bit.",
             "more": "Business verification runs through a verified representative today; a full KYB flow is on the roadmap.", "roadmap": "KYB flow"},
            {"label": "Mandate applied", "text": "Ceiling, permitted counterparties and jurisdictions are tested against the transfer.",
             "more": "Today the mandate carries amount, counterparty and expiry rules. Sanctions screening results feeding the gate is a roadmap item.", "roadmap": "Screening input"},
            {"label": "The gate decides", "text": "Trust gate, then money gate: allow, escalate or deny.", "more": GATE_MORE},
            {"label": "Settlement with proof", "text": "The transfer executes with a decision token and receipt; the decision is anchored.",
             "more": "Live today for x402 stablecoin payments on get4agent.com; the receipt carries the decision id and the settlement reference."},
            {"label": "Guardian and kill switch", "text": "Anomalies are flagged over transaction patterns; suspension reaches every verifier within seconds.",
             "more": KILL_MORE},
        ],
        "gives": [
            {"dim": "Revenue", "h": "Institutional counterparties", "p": "Serve regulated entities that cannot touch unverified flows."},
            {"dim": "Cost", "h": "Screening starts from a verified owner", "p": "Less manual triage than working from a bare address."},
            {"dim": "Risk", "h": "Value does not move outside a mandate", "p": "The gate denies what the mandate does not allow."},
            {"dim": "Speed", "h": "Faster settlement", "p": "Verified agents settle without waiting on ad-hoc counterparty checks."},
        ],
        "before": "Participation is limited to a few pre-approved counterparties: slow, rigid and hard to scale.",
        "after": "Any properly mandated agent can settle within verified bounds, with a decision token and receipt for each action.",
        "subcase": None,
        "drawer": [
            {"h": "Where the proof lives", "items": [
                "Decision and receipt are signed off-chain; the audit batch (Merkle root) is anchored on Solana; the settlement reference is recorded in the receipt.",
                "Solana devnet today; mainnet after the program audit.",
            ]},
            {"h": "Gate check pattern in a settlement flow", "items": [
                "Agent → gate → allow → transfer submitted → receipt with the transaction reference.",
                "Deny: nothing is submitted, nothing moves, the refusal is recorded.",
                {"text": "On-chain enforcement: a program that moves funds only with a valid Regent decision token.", "roadmap": True},
            ]},
            {"h": "Screening and jurisdictions", "items": [
                "Permitted counterparties and jurisdictions are mandate rules today.",
                {"text": "Sanctions screening result as an input to the gate.", "roadmap": True},
                {"text": "KYB verification flow for business owners.", "roadmap": True},
            ]},
            {"h": "Kill-switch propagation", "items": [
                "A verifier checks the agent status or the receipt with Regent; a revoked agent is refused within seconds.",
            ]},
            {"h": "Deployment", "items": [
                "Regent's cloud, a dedicated instance in your region, or the sidecar inside your perimeter; the same gate and the same receipts.",
            ]},
        ],
    },
]
