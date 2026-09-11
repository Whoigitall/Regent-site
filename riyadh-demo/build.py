#!/usr/bin/env python3
"""Build the self-contained Money20/20 Riyadh demo page.

  python3 build.py            -> writes ../v2-static/riyadh/index.html, copy-deck.md, prints size + banned-string scan

Everything the page needs (fonts, logo, QR data) is read from ./assets and inlined. No network at runtime.
"""
import base64, html, json, math, os, re, sys
from data import EVENT, CTA, POSITIONING, NUMBERS, SEGMENTS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "v2-static", "riyadh")
ASSETS = os.path.join(HERE, "assets")

def esc(s):
    return html.escape(str(s), quote=False)

def attr(s):
    return html.escape(str(s), quote=True)

def b64(name):
    with open(os.path.join(ASSETS, name), "rb") as f:
        return base64.b64encode(f.read()).decode()

QR = json.load(open(os.path.join(ASSETS, "qr.json")))

# ---------------------------------------------------------------- SVG helpers
def hexagon(cx, cy, r):
    pts = []
    for k in range(6):
        a = math.radians(90 + 60 * k)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy - r * math.sin(a):.1f}")
    return " ".join(pts)

def badge(x, y, n):
    return (f'<g class="sb"><circle cx="{x}" cy="{y}" r="12"/>'
            f'<text x="{x}" y="{y + 4.5}" text-anchor="middle">{n}</text></g>')

def gate(cx, cy, label):
    return (f'<g class="gate" transform="translate({cx},{cy})">'
            f'<rect class="door" x="-16" y="-30" width="32" height="60" rx="4"/>'
            f'<rect class="post" x="-26" y="-34" width="8" height="68" rx="2"/>'
            f'<rect class="post" x="18" y="-34" width="8" height="68" rx="2"/>'
            f'<rect class="post" x="-30" y="-40" width="60" height="7" rx="2"/>'
            f'<text class="lbl" x="0" y="58" text-anchor="middle">{esc(label)}</text></g>')

def pill(x, y, w, text, cls, extra=""):
    return (f'<g class="pill {cls}" transform="translate({x},{y})">'
            f'<rect x="{-w/2}" y="-13" width="{w}" height="26" rx="13"/>'
            f'<text x="0" y="4.5" text-anchor="middle">{esc(text)}</text>{extra}</g>')

def tick(x, y, r=10):
    return (f'<g transform="translate({x},{y})"><circle r="{r}" class="tickc"/>'
            f'<path class="tickp" d="M-4.5 0.5 L-1.5 3.5 L5 -3.5"/></g>')

def svg_flow(seg):
    sid = seg["id"]
    chip0 = seg["chips"][0]
    org = seg["org"]
    packet = chip0["packet"]
    # main path agent -> gate1 -> gate2 -> packet -> org (used for the kill overlay)
    kill_d = "M188 150 L374 150 M426 150 L514 150 M566 150 L660 150 M790 150 L860 150"
    s = []
    s.append(f'<svg class="dg-svg" viewBox="0 0 1000 400" role="img" aria-labelledby="t-{sid} d-{sid}" focusable="false">')
    s.append(f'<title id="t-{sid}">Decision map: {esc(seg["label"])}</title>')
    s.append(f'<desc id="d-{sid}">An agent with an AgentID passport and a verified owner is tested against its mandate, passes the trust gate and the money gate, and the transaction carries a decision token and a signed receipt into the {esc(org.lower())}; the decision is anchored, Guardian watches behaviour and the owner holds the kill switch.</desc>')
    s.append('<defs><marker id="arr-' + sid + '" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z"/></marker>'
             '<filter id="glow-' + sid + '" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    m = f'marker-end="url(#arr-{sid})"'
    # connectors
    s.append(f'<g class="st cn" data-s="2"><path class="con" d="M140 228 L140 274" {m}/><path class="con flow" d="M140 228 L140 274"/></g>')
    s.append(f'<g class="st cn" data-s="4"><path class="con" d="M188 150 L374 150" {m}/><path class="con flow" d="M188 150 L374 150"/></g>')
    s.append(f'<g class="st cn" data-s="4"><path class="con" d="M426 150 L514 150" {m}/><path class="con flow" d="M426 150 L514 150"/></g>')
    s.append(f'<g class="st cn br br-allow" data-s="4"><path class="con" d="M566 150 L660 150" {m}/><path class="con flow" d="M566 150 L660 150"/></g>')
    s.append(f'<g class="st cn br br-escalate" data-s="4"><path class="con" d="M566 140 C 600 140, 606 64, 640 64" {m}/><path class="con flow" d="M566 140 C 600 140, 606 64, 640 64"/></g>')
    s.append(f'<g class="st cn br br-deny" data-s="4"><path class="con" d="M566 160 C 600 160, 606 236, 640 236" {m}/><path class="con flow" d="M566 160 C 600 160, 606 236, 640 236"/></g>')
    s.append(f'<g class="st cn" data-s="5"><path class="con" d="M790 150 L860 150" {m}/><path class="con flow" d="M790 150 L860 150"/></g>')
    s.append(f'<g class="st cn" data-s="6"><path class="con" d="M725 180 L725 318" {m}/><path class="con flow" d="M725 180 L725 318"/></g>')
    # 1 agent passport
    s.append(f'<g class="st node n1" data-s="1" tabindex="0" data-tip="AgentID (passport): a unique, checkable identity for the AI agent. Identity only; it grants no authority.">'
             f'<title>AgentID (passport)</title>'
             f'<polygon class="hex" points="{hexagon(140,150,48)}"/>'
             f'<circle class="ring" cx="140" cy="150" r="58"/>'
             f'<text class="lbl big" x="140" y="146" text-anchor="middle">AgentID</text>'
             f'<text class="lbl mono" x="140" y="166" text-anchor="middle">passport</text>'
             f'{badge(86, 98, 1)}</g>')
    # 3 mandate frame (drawn before owner so the owner sits on top visually)
    s.append(f'<g class="st node n3" data-s="3" tabindex="0" data-tip="mandate: what the agent may do. Scope, ceiling, permitted counterparties, expiry.">'
             f'<title>mandate</title>'
             f'<rect class="frame" x="66" y="76" width="148" height="152" rx="14"/>'
             f'<text class="lbl mono" x="140" y="220" text-anchor="middle">mandate</text>'
             f'<g transform="translate(232,92)"><g class="oof"><rect x="0" y="0" width="22" height="22" rx="5"/><path d="M6 6 L16 16 M16 6 L6 16"/></g></g>'
             f'{badge(226, 76, 3)}</g>')
    # 2 owner
    s.append(f'<g class="st node n2" data-s="2" tabindex="0" data-tip="verified owner: the human or business the agent acts for. Only one bit leaves Regent: verified.">'
             f'<title>verified owner</title>'
             f'<circle class="owner" cx="140" cy="300" r="24"/>'
             f'{tick(140,300,11)}'
             f'<text class="lbl" x="140" y="342" text-anchor="middle">verified owner</text>'
             f'<text class="lbl mono dim" x="140" y="358" text-anchor="middle">1 bit outward</text>'
             f'{badge(176, 274, 2)}</g>')
    # 4 gates + outcomes
    s.append(f'<g class="st node n4" data-s="4" tabindex="0" data-tip="the gate: trust gate, then money gate. One of three outcomes: allow, escalate or deny.">'
             f'<title>the gate (trust gate + money gate)</title>'
             f'{gate(400,150,"trust gate")}{gate(540,150,"money gate")}'
             f'<g class="br br-allow">{pill(612,136,58,"allow","p-allow")}</g>'
             f'<g class="br br-escalate">{pill(694,64,94,"escalate","p-esc")}</g>'
             f'<g class="br br-deny">{pill(680,236,64,"deny","p-deny")}</g>'
             f'{badge(470, 96, 4)}</g>')
    # 5 packet + seal + receipt + org
    s.append(f'<g class="st node n5" data-s="5" tabindex="0" data-tip="decision token + signed receipt: the proof attached to the action, and the signed record of the decision.">'
             f'<title>decision token + signed receipt</title>'
             f'<rect class="packet" x="660" y="120" width="130" height="60" rx="10"/>'
             f'<text class="lbl big" id="pk-{sid}" x="720" y="155" text-anchor="middle">{esc(packet)}</text>'
             f'<g transform="translate(790,120)"><g class="seal"><circle r="17"/><path class="tickp" d="M-6 0.5 L-2 4.5 L7 -4.5"/></g></g>'
             f'<rect class="stub" x="684" y="188" width="82" height="20" rx="4"/>'
             f'<text class="lbl mono stubt" x="725" y="202" text-anchor="middle">receipt</text>'
             f'<rect class="org" x="860" y="110" width="120" height="80" rx="12"/>'
             f'<text class="lbl big" id="org-{sid}" x="920" y="155" text-anchor="middle">{esc(org)}</text>'
             f'{badge(646, 108, 5)}</g>')
    # 6 audit + guardian + kill
    cells = "".join(f'<rect class="cell" style="--i:{i}" x="{386 + i*49}" y="323" width="44" height="24" rx="4"/>' for i in range(8))
    s.append(f'<g class="st node n6" data-s="6" tabindex="0" data-tip="anchored audit, Guardian and kill switch: the decision is anchored; Guardian scores behaviour; the owner can suspend the agent for every verifier that checks with Regent.">'
             f'<title>anchored audit · Guardian · kill switch</title>'
             f'<rect class="strip" x="380" y="318" width="400" height="34" rx="6"/>{cells}'
             f'<text class="lbl mono" x="386" y="308">anchored audit</text>'
             f'<g transform="translate(900,330)"><circle class="radar" r="30"/><circle class="radar2" r="18"/>'
             f'<g class="sweep"><line x1="0" y1="0" x2="0" y2="-30"/></g><circle class="anom" cx="12" cy="-14" r="4"/></g>'
             f'<text class="lbl mono" x="900" y="380" text-anchor="middle">Guardian</text>'
             f'<path class="kill" d="{kill_d}"/>'
             f'<text class="lbl mono killt" x="300" y="380" text-anchor="middle">kill switch: revoked, seen by every verifier</text>'
             f'{badge(358, 298, 6)}</g>')
    s.append('</svg>')
    return "".join(s)

def svg_record(seg):
    sid = seg["id"]
    s = []
    s.append(f'<svg class="dg-svg" viewBox="0 0 1000 400" role="img" aria-labelledby="t-{sid} d-{sid}" focusable="false">')
    s.append(f'<title id="t-{sid}">Decision record: {esc(seg["label"])}</title>')
    s.append(f'<desc id="d-{sid}">Inside Regent: a registry of AgentID passports with live status and the anchored decisions attached to them. Outward, only one bit about a person: verified. A verifier sees a revocation within seconds; the record answers who authorised what under which mandate; aggregate supervision views are a roadmap item.</desc>')
    s.append('<defs><marker id="arr-' + sid + '" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z"/></marker></defs>')
    m = f'marker-end="url(#arr-{sid})"'
    # boundary
    s.append('<g class="st bnd" data-s="1"><rect class="boundary" x="40" y="40" width="560" height="330" rx="16"/>'
             '<text class="lbl mono" x="56" y="62">inside Regent</text></g>')
    # 1 registry
    ys = [120, 210, 300]
    st = [("active", "p-allow"), ("active", "p-allow"), ("revoked", "p-deny")]
    reg = ""
    for i, y in enumerate(ys):
        reg += (f'<polygon class="hex" points="{hexagon(120, y, 28)}"/>'
                f'<text class="lbl mono" x="120" y="{y+4}" text-anchor="middle">AgentID</text>'
                f'{pill(196, y, 70, st[i][0], st[i][1])}')
    s.append(f'<g class="st node n1" data-s="1" tabindex="0" data-tip="AgentID registry: agent credentials with a live status. A registry of agents, not of people.">'
             f'<title>AgentID registry</title>{reg}{badge(80, 86, 1)}</g>')
    # connectors registry -> decisions
    for i, y in enumerate(ys):
        s.append(f'<g class="st cn" data-s="2"><path class="con" d="M232 {y} L300 {y}" {m}/><path class="con flow" d="M232 {y} L300 {y}"/></g>')
    # 2 decisions
    rows = [("allow", "p-allow"), ("escalate", "p-esc"), ("deny", "p-deny")]
    dec = ""
    for i, y in enumerate(ys):
        dec += (f'<rect class="row" x="300" y="{y-18}" width="250" height="36" rx="8"/>'
                f'{pill(348, y, 74, rows[i][0], rows[i][1])}'
                f'<rect class="stub" x="400" y="{y-9}" width="60" height="18" rx="4"/>'
                f'<text class="lbl mono stubt" x="430" y="{y+4}" text-anchor="middle">receipt</text>'
                f'<text class="lbl mono dim" x="478" y="{y+4}">anchored</text>')
    s.append(f'<g class="st node n2" data-s="2" tabindex="0" data-tip="anchored audit: every allow, escalate or deny is recorded with its evidence and anchored.">'
             f'<title>anchored decisions</title>{dec}{badge(300, 86, 2)}</g>')
    # 3 one bit outward
    s.append(f'<g class="st cn" data-s="3"><path class="con" d="M600 200 L700 200" {m}/><path class="con flow" d="M600 200 L700 200"/></g>')
    s.append(f'<g class="st node n3" data-s="3" tabindex="0" data-tip="one bit outward: about a person, only verified leaves Regent. Names, reasons, history and reputation stay inside.">'
             f'<title>one bit outward</title>'
             f'<g transform="translate(600,200)"><g class="bit">{tick(0,0,12)}</g></g>'
             f'<text class="lbl mono" x="650" y="184" text-anchor="middle">verified</text>'
             f'<rect class="org" x="700" y="170" width="150" height="60" rx="12"/>'
             f'<text class="lbl big" x="775" y="196" text-anchor="middle">verifier</text>'
             f'<text class="lbl mono dim" x="775" y="214" text-anchor="middle">bank · platform</text>'
             f'<text class="lbl mono dim" x="560" y="356" text-anchor="end">name · reasons · history stay inside</text>'
             f'{badge(600, 160, 3)}</g>')
    # 4 kill switch along the verification path
    s.append(f'<g class="st node n4" data-s="4" tabindex="0" data-tip="kill switch: the owner or its institution suspends an agent; every verifier that checks with Regent sees it within seconds.">'
             f'<title>kill switch</title>'
             f'<path class="kill" d="M232 300 C 560 300, 640 232, 700 218"/>'
             f'<text class="lbl mono killt" x="470" y="296" text-anchor="middle">revoked · seen by the verifier</text>'
             f'{badge(470, 320, 4)}</g>')
    # 5 query panel
    s.append(f'<g class="st node n5" data-s="5" tabindex="0" data-tip="evidence in investigations: a decision resolves to its agent, mandate and outcome, and the receipt verifies against public keys.">'
             f'<title>evidence in investigations</title>'
             f'<rect class="panelr" x="700" y="252" width="270" height="112" rx="10"/>'
             f'<text class="lbl mono" x="716" y="276">query one decision</text>'
             f'<text class="lbl mono q1" x="716" y="298">dec_5fb4e9e0e446 → agent → mandate</text>'
             f'<text class="lbl mono q2" x="716" y="318">outcome: allow · receipt verified</text>'
             f'<text class="lbl mono dim" x="716" y="340">authority access:</text>'
             f'<text class="lbl mono dim" x="716" y="354">a legal-basis question, not a feature</text>'
             f'{badge(700, 242, 5)}</g>')
    # 6 roadmap
    s.append(f'<g class="st node n6 rmap" data-s="6" tabindex="0" data-tip="Roadmap: aggregate supervision views and supervisory reporting are not available today.">'
             f'<title>aggregate supervision (roadmap)</title>'
             f'<rect class="roadbox" x="700" y="60" width="270" height="80" rx="10"/>'
             f'<text class="lbl" x="716" y="90">aggregate views · reporting</text>'
             f'{pill(930, 84, 74, "Roadmap", "p-road")}'
             f'<text class="lbl mono dim" x="716" y="118">not available today</text>'
             f'{badge(700, 50, 6)}</g>')
    s.append('</svg>')
    return "".join(s)

def svg_arch():
    return ('<svg class="arch-svg" viewBox="0 0 1000 220" role="img" aria-labelledby="t-arch d-arch">'
            '<title id="t-arch">One decision layer for four segments</title>'
            '<desc id="d-arch">Banks, commerce platforms, regulators and settlement rails all point their agents at the same two gates; every decision produces a decision token, a signed receipt and an anchored audit entry.</desc>'
            '<defs><marker id="arr-arch" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z"/></marker></defs>'
            + "".join(f'<g class="on st"><rect class="org" x="30" y="{20+i*48}" width="200" height="36" rx="8"/><text class="lbl" x="130" y="{43+i*48}" text-anchor="middle">{t}</text>'
                      f'<path class="con" d="M230 {38+i*48} C 300 {38+i*48}, 320 110, 372 110" marker-end="url(#arr-arch)"/></g>'
                      for i, t in enumerate(["Banks & financial institutions", "Commerce & platforms", "Regulators & compliance", "Stablecoin & tokenised settlement"]))
            + f'<g class="on st active">{gate(420,110,"trust gate")}{gate(540,110,"money gate")}</g>'
            '<g class="on st"><path class="con" d="M566 110 L640 110" marker-end="url(#arr-arch)"/>'
            '<rect class="packet" x="640" y="80" width="150" height="60" rx="10"/><text class="lbl big" x="715" y="106" text-anchor="middle">decision token</text><text class="lbl mono" x="715" y="126" text-anchor="middle">+ signed receipt</text>'
            '<path class="con" d="M790 110 L840 110" marker-end="url(#arr-arch)"/>'
            '<rect class="strip" x="840" y="92" width="140" height="36" rx="6"/><text class="lbl mono" x="910" y="115" text-anchor="middle">anchored audit</text></g>'
            '</svg>')

# ---------------------------------------------------------------- icons
ICONS = {
    "wallet": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M16 14h2"/>',
    "key": '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/>',
    "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
    "bot": '<rect x="4" y="8" width="16" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01M2 13h2M20 13h2"/>',
    "traffic": '<path d="M4 18h16M6 14l3-6 3 4 3-8 3 10"/>',
    "ticket": '<path d="M4 8a2 2 0 0 0 2-2h12a2 2 0 0 0 2 2v3a2 2 0 0 0 0 4v3a2 2 0 0 0-2 2H6a2 2 0 0 0-2-2v-3a2 2 0 0 0 0-4z"/><path d="M12 7v10"/>',
    "scale": '<path d="M12 4v16M5 8h14M7 8l-3 6h6zM17 8l-3 6h6zM8 20h8"/>',
    "eye": '<path d="M2 12s4-6 10-6 10 6 10 6-4 6-10 6S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "switch": '<rect x="3" y="8" width="18" height="8" rx="4"/><circle cx="16" cy="12" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
}
def icon(name):
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

# ---------------------------------------------------------------- HTML pieces
def rm(text="Roadmap"):
    return f'<span class="rm">{esc(text)}</span>'

def render_segment(seg):
    sid = seg["id"]
    chips = "".join(
        f'<button class="chip{" is-on" if i == 0 else ""}" type="button" role="radio" aria-checked="{"true" if i == 0 else "false"}" '
        f'data-path="{attr(c.get("path", ""))}" data-packet="{attr(c.get("packet", ""))}" data-focus="{attr(c.get("focus", ""))}" '
        f'data-scenario="{attr(c["scenario"])}">{esc(c["name"])}</button>'
        for i, c in enumerate(seg["chips"]))
    why = "".join(f'<div class="card why"><div class="ico-w">{icon(w["icon"])}</div><h3>{esc(w["h"])}</h3><p>{esc(w["p"])}</p></div>' for w in seg["why"])
    steps_li = ""
    for i, st in enumerate(seg["steps"], 1):
        flag = rm("Roadmap") if st.get("roadmap") else ""
        steps_li += (f'<li class="step" data-i="{i}"><button type="button" class="step-btn" aria-current="false">'
                     f'<span class="num">{i}</span><span class="st-l">{esc(st["label"])}{flag}</span>'
                     f'<span class="st-t">{esc(st["text"])}</span></button>'
                     f'<button type="button" class="more-btn" aria-expanded="false" aria-controls="m-{sid}-{i}">Learn more</button>'
                     f'<div class="more" id="m-{sid}-{i}"><div><p>{esc(st["more"])}</p></div></div></li>')
    text_version = "".join(f'<li><strong>{esc(st["label"])}.</strong> {esc(st["text"])}</li>' for st in seg["steps"])
    gives = "".join(f'<div class="card give"><span class="dim">{esc(g["dim"])}</span><h3>{esc(g["h"])}</h3><p>{esc(g["p"])}</p></div>' for g in seg["gives"])
    sub = ""
    if seg.get("subcase"):
        sub = f'<p class="subcase"><span class="dim">{esc(seg["subcase"]["h"])} sub-case</span> {esc(seg["subcase"]["p"])}</p>'
    drawer = ""
    for sec in seg["drawer"]:
        items = ""
        for it in sec["items"]:
            if isinstance(it, dict):
                items += f'<li>{esc(it["text"])} {rm()}</li>'
            else:
                items += f'<li>{esc(it)}</li>'
        drawer += f'<div class="dsec"><h4>{esc(sec["h"])}</h4><ul>{items}</ul></div>'
    svg = svg_record(seg) if seg["variant"] == "record" else svg_flow(seg)
    default_path = seg["chips"][0].get("path", "")
    return f'''
<section class="panel" id="{sid}" role="tabpanel" aria-labelledby="tab-{sid}" tabindex="0" data-variant="{seg["variant"]}">
  <header class="p-head">
    <h2>{esc(seg["label"])}</h2>
    <p class="promise">{esc(seg["promise"])}</p>
    <div class="chips" role="radiogroup" aria-label="Scenario">{chips}</div>
    <p class="scenario"><span class="dim">Scenario</span> <span class="scenario-t">{esc(seg["chips"][0]["scenario"])}</span></p>
  </header>

  <div class="strip3">{why}</div>

  <figure class="dg" data-step="0" data-path="{attr(default_path)}" aria-label="Animated decision map">
    <div class="dg-wrap">{svg}</div>
    <div class="dg-side">
      <div class="dg-ctl" role="group" aria-label="Diagram controls">
        <button type="button" class="btn sm play" aria-pressed="false">Play</button>
        <button type="button" class="btn sm restart">Restart</button>
        <span class="dg-pos mono" aria-live="polite">Step 0 of 6</span>
      </div>
      <ol class="steps">{steps_li}</ol>
    </div>
    <figcaption class="textv"><details><summary>Text version of this diagram</summary><ol>{text_version}</ol></details></figcaption>
  </figure>

  <h3 class="h-sec">What this gives you</h3>
  <div class="strip4">{gives}</div>

  <div class="ba">
    <div class="card"><span class="dim">Before</span><p>{esc(seg["before"])}</p></div>
    <div class="card is-after"><span class="dim">After</span><p>{esc(seg["after"])}</p></div>
  </div>
  {sub}

  <div class="drawer">
    <button type="button" class="drawer-btn" aria-expanded="false" aria-controls="dr-{sid}"><span>Learn more</span><span class="dim">technical depth for this segment</span></button>
    <div class="drawer-body" id="dr-{sid}"><div class="drawer-in">{drawer}</div></div>
  </div>

  <div class="tab-cta">
    <p>{esc(CTA["closing"])}</p>
    <a class="btn primary" href="{attr(CTA["url"])}" target="_blank" rel="noopener">{esc(CTA["label"])}</a>
  </div>
</section>'''

def render_numbers():
    items = "".join(f'<div class="num-i"><span class="n">{esc(x["n"])}</span><span class="l mono">{esc(x["label"])}</span><span class="t">{esc(x["note"])}</span></div>' for x in NUMBERS["items"])
    return f'''<section class="numbers" aria-label="In production">
  <div class="wrap">
    <div class="num-head"><span class="mono">In production</span><span class="dim">{esc(NUMBERS["as_of"])}</span></div>
    <div class="num-grid">{items}</div>
    <p class="bench">{esc(NUMBERS["bench"])}</p>
  </div></section>'''

def qr_svg(key, size):
    q = QR[key]
    return (f'<svg class="qr" viewBox="{attr(q["viewBox"])}" width="{size}" height="{size}" role="img" aria-hidden="true">'
            f'<rect width="100%" height="100%" fill="#fff"/><path d="{q["d"]}" fill="#0F1513"/></svg>')

# ---------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:"Orbitron";font-style:normal;font-weight:600;font-display:swap;src:url(data:font/woff2;base64,%ORBITRON%) format("woff2")}
@font-face{font-family:"Oxanium";font-style:normal;font-weight:200 800;font-display:swap;src:url(data:font/woff2;base64,%OXANIUM%) format("woff2")}
@font-face{font-family:"Geist Mono";font-style:normal;font-weight:400;font-display:swap;src:url(data:font/woff2;base64,%GEISTMONO%) format("woff2")}
:root{
  /* light theme = default (site light palette) */
  color-scheme:light;
  --bg:#F7F7F3;--panel:#FFFFFF;--card:#FFFFFF;--panel2:#F1F3EE;--hair:#E7EAE3;--line:#D9DDD6;
  --ink:#16211E;--mut:#55625D;--faint:#82908A;
  --seal:#007A6E;--seal-hi:#009C8C;--seal-soft:#DFF2EF;--seal-soft2:#C6E8E1;--seal-rgb:0,122,110;--on-seal:#FFFFFF;
  --allow:#1E6B45;--allow-hi:#1E6B45;--esc:#9A6A14;--esc-hi:#9A6A14;--deny:#A03227;--deny-hi:#C23A2C;--roadmap:#6B7A88;
  --topbg:rgba(247,247,243,.92);--tipbg:#FFFFFF;--logo-invert:1;
  --f-head:"Orbitron","Oxanium",system-ui,sans-serif;--f-body:"Oxanium","Segoe UI",system-ui,-apple-system,sans-serif;--f-mono:"Geist Mono",ui-monospace,Menlo,Consolas,monospace;
  --radius:14px;--radius-sm:9px;--shadow:0 20px 60px rgba(0,0,0,.18);
  --dur-fast:180ms;--dur:240ms;--dur-slow:800ms;--ease:cubic-bezier(.22,.61,.36,1);
  --top:56px;--tabs:52px;
}
:root[data-theme="dark"]{
  color-scheme:dark;
  --bg:#0F1513;--panel:#111716;--card:#151C19;--panel2:#0E1412;--hair:#1E2723;--line:#28312D;
  --ink:#E7EBE6;--mut:#9AA8A1;--faint:#6D7B75;
  --seal:#00C9B7;--seal-hi:#19D3BC;--seal-soft:#0C2723;--seal-soft2:#0F3A34;--seal-rgb:0,201,183;--on-seal:#04211D;
  --allow:#64B98A;--allow-hi:#3FE08A;--esc:#D6A44C;--esc-hi:#D9B24C;--deny:#E07A6E;--deny-hi:#FF4D5E;--roadmap:#8A9AA8;
  --topbg:rgba(15,21,19,.92);--tipbg:#0B100E;--logo-invert:0;
  --shadow:0 20px 60px rgba(0,0,0,.5);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.6 var(--f-body);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--seal)}
h1,h2,h3,h4{margin:0;line-height:1.2;font-weight:600;text-wrap:balance}
p{margin:0}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.mono{font-family:var(--f-mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.dim{font-family:var(--f-mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--faint)}
.skip{position:absolute;left:-999px;top:8px;background:var(--seal);color:var(--on-seal);padding:8px 12px;border-radius:8px;z-index:100}
.skip:focus{left:8px}
:focus-visible{outline:2px solid var(--seal);outline-offset:2px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:10px 18px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:600 14px/1 var(--f-body);text-decoration:none;cursor:pointer;transition:border-color var(--dur) var(--ease),background var(--dur) var(--ease)}
.btn:hover{border-color:rgba(var(--seal-rgb),.5)}
.btn.primary{background:var(--seal);border-color:var(--seal);color:var(--on-seal)}
.btn.primary:hover{background:var(--seal-hi)}
.btn.sm{min-height:36px;padding:6px 14px;font-size:13px}
.rm{display:inline-flex;align-items:center;margin-left:8px;padding:2px 8px;border-radius:999px;font:400 11px/1.5 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--roadmap);background:rgba(138,154,168,.12);border:1px solid rgba(138,154,168,.3);vertical-align:middle}

/* top bar */
.top{position:sticky;top:0;z-index:50;height:var(--top);background:var(--topbg);backdrop-filter:blur(10px);border-bottom:1px solid var(--hair)}
.top .wrap{height:100%;display:flex;align-items:center;gap:16px}
.brand{display:flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none}
.brand img.ic{width:22px;height:auto;filter:invert(var(--logo-invert))}
.brand img.wm{height:11px;width:auto;filter:invert(var(--logo-invert))}
.badge{font-family:var(--f-mono);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);border:1px solid var(--line);border-radius:999px;padding:5px 10px;white-space:nowrap}
.top .grow{flex:1}
.lang{font-family:var(--f-mono);font-size:11.5px;color:var(--faint);letter-spacing:.06em}
.theme{min-height:36px;padding:6px 12px;font:400 11.5px/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase}
.theme .d{display:none}
:root[data-theme="dark"] .theme .l{display:none}
:root[data-theme="dark"] .theme .d{display:inline}
@media(max-width:720px){.badge{display:none}.top .btn{padding:8px 12px;font-size:13px}}
@media(max-width:480px){.lang{display:none}.theme{display:none}.brand img.wm{height:9px}.brand img.ic{width:18px}.top .btn{font-size:12px;padding:8px 10px;min-height:38px}.top .wrap{gap:10px;padding:0 14px}}

/* hero */
.hero{padding:56px 0 28px}
.hero h1{max-width:980px}
.hero .k{display:block;font:600 18px/1.4 var(--f-body);color:var(--mut);margin-bottom:12px}
.hero .loud{display:block;font:600 clamp(24px,3.6vw,40px)/1.18 var(--f-head);letter-spacing:.005em;color:var(--ink)}
.hero .loud em{font-style:normal;color:var(--seal)}
.hero .lead{margin:20px 0 0;max-width:66ch;color:var(--mut)}
.seg-chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.seg-chips a{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:8px 16px;border:1px solid var(--line);border-radius:999px;color:var(--ink);text-decoration:none;font-weight:600;font-size:14px;background:var(--panel)}
.seg-chips a:hover{border-color:rgba(var(--seal-rgb),.45)}
.seg-chips a .mono{color:var(--faint)}

/* numbers */
.numbers{padding:24px 0 8px}
.numbers .wrap>div,.numbers .wrap>p{border-top:1px solid var(--hair)}
.num-head{display:flex;justify-content:space-between;gap:12px;padding:14px 0 6px;flex-wrap:wrap}
.num-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;padding:12px 0 16px;border-top:0!important}
.num-i{display:flex;flex-direction:column;gap:4px}
.num-i .n{font:600 28px/1.1 var(--f-body);font-variant-numeric:tabular-nums;color:var(--ink)}
.num-i .t{font-size:13px;color:var(--faint);line-height:1.4}
.bench{padding:12px 0 0;font-size:13.5px;color:var(--mut);max-width:80ch}
@media(max-width:960px){.num-grid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:600px){.num-grid{grid-template-columns:repeat(2,1fr)}}

/* tabs */
.tabs{position:sticky;top:var(--top);z-index:40;background:var(--topbg);backdrop-filter:blur(10px);border-bottom:1px solid var(--hair);margin-top:24px}
.tabs .wrap{position:relative}
.tablist{display:flex;gap:4px;overflow-x:auto;scrollbar-width:none;-ms-overflow-style:none}
.tablist::-webkit-scrollbar{display:none}
.tab{position:relative;flex:0 0 auto;min-height:var(--tabs);padding:0 16px;border:0;background:none;color:var(--mut);font:600 12px/1 var(--f-head);letter-spacing:.04em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.tab[aria-selected="true"]{color:var(--ink)}
.tab:hover{color:var(--ink)}
.ind{position:absolute;bottom:-1px;height:2px;background:var(--seal);left:0;width:0;transition:left 220ms ease-out,width 220ms ease-out}
html:not(.js) .ind{display:none}

/* panels */
.panels{padding-bottom:24px}
.panel{padding:56px 0 24px;border-bottom:1px solid var(--hair);scroll-margin-top:calc(var(--top) + var(--tabs) + 8px)}
html.js .panel{display:none}
html.js .panel.is-active{display:block;animation:rise 200ms var(--ease) 1}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.panel>*{max-width:1200px;margin-left:auto;margin-right:auto;padding-left:24px;padding-right:24px}
.p-head h2{font:600 clamp(20px,2.6vw,28px)/1.2 var(--f-head);letter-spacing:.01em}
.promise{margin-top:10px;font:600 clamp(19px,2.2vw,24px)/1.3 var(--f-body);color:var(--seal);max-width:66ch;text-wrap:balance}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.chip{min-height:32px;padding:5px 14px;border-radius:999px;border:1px solid var(--line);background:transparent;color:var(--mut);font:600 13px/1.2 var(--f-body);cursor:pointer;transition:all var(--dur) var(--ease)}
.chip:hover{color:var(--ink);border-color:rgba(var(--seal-rgb),.45)}
.chip.is-on{color:var(--seal);border-color:var(--seal);background:rgba(var(--seal-rgb),.08)}
.scenario{margin-top:12px;color:var(--mut);max-width:80ch;font-size:15px}
.scenario .dim{margin-right:8px}
.strip3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:32px}
.strip4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:24px;transition:border-color var(--dur) var(--ease)}
.card:hover{border-color:rgba(var(--seal-rgb),.3)}
.card h3{font-size:17px;margin:12px 0 8px}
.card p{color:var(--mut);font-size:15px}
.card .dim{display:block}
.why .ico-w{width:36px;height:36px;border-radius:10px;background:var(--seal-soft);display:grid;place-items:center;color:var(--seal)}
.ico{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.give h3{color:var(--ink)}
.give:first-child .dim{color:var(--seal)}
.h-sec{margin-top:40px;font:600 12.5px/1.4 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}
.ba{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:32px}
.ba .card p{color:var(--ink);margin-top:10px;font-size:15.5px}
.ba .is-after{border-color:rgba(var(--seal-rgb),.35)}
.subcase{margin-top:16px;color:var(--mut);font-size:15px;max-width:80ch}
.subcase .dim{margin-right:8px}
@media(max-width:960px){.strip3{grid-template-columns:1fr 1fr 1fr}.strip4{grid-template-columns:1fr 1fr}}
@media(max-width:720px){.strip3,.strip4,.ba{grid-template-columns:1fr}.panel{padding-top:40px}}

/* drawer */
.drawer{margin-top:28px;border:1px solid var(--line);border-radius:var(--radius);background:var(--panel)}
.drawer-btn{width:100%;display:flex;justify-content:space-between;align-items:center;gap:12px;padding:16px 20px;background:none;border:0;color:var(--ink);font:600 15px/1.2 var(--f-body);cursor:pointer;text-align:left;border-radius:var(--radius)}
.drawer-btn::after{content:"+";font-family:var(--f-mono);color:var(--seal);font-size:18px;margin-left:auto}
.drawer-btn[aria-expanded="true"]::after{content:"–"}
.drawer-body{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--dur-slow) var(--ease)}
.drawer-body>div{overflow:hidden;min-height:0}
.drawer-btn[aria-expanded="true"]+.drawer-body{grid-template-rows:1fr}
html:not(.js) .drawer-body{grid-template-rows:1fr}
.drawer-in{padding:0 20px 20px;display:grid;grid-template-columns:1fr 1fr;gap:20px 32px}
.dsec h4{font:600 12.5px/1.4 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;color:var(--seal);margin-bottom:8px}
.dsec ul{margin:0;padding-left:18px;color:var(--mut);font-size:14.5px}
.dsec li{margin:6px 0}
@media(max-width:720px){.drawer-in{grid-template-columns:1fr}}
.tab-cta{margin-top:28px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;padding:20px 24px;border-radius:var(--radius);background:var(--seal-soft);border:1px solid rgba(var(--seal-rgb),.25)}
.tab-cta p{font-weight:600;max-width:60ch}

/* diagram layout */
.dg{margin:32px auto 0;display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:20px;align-items:start}
.dg-wrap{background:var(--panel2);border:1px solid var(--hair);border-radius:var(--radius);padding:10px;overflow:hidden}
.dg-svg{width:100%;height:auto;display:block;font-family:var(--f-body)}
.dg-side{display:flex;flex-direction:column;gap:12px}
.dg-ctl{display:flex;align-items:center;gap:8px}
.dg-pos{margin-left:auto}
.steps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.step{border:1px solid transparent;border-radius:var(--radius-sm);transition:border-color var(--dur) var(--ease),background var(--dur) var(--ease)}
.step.is-active{border-color:rgba(var(--seal-rgb),.35);background:var(--card)}
.step-btn{display:grid;grid-template-columns:24px 1fr;gap:4px 10px;width:100%;padding:8px 10px;background:none;border:0;color:var(--ink);text-align:left;cursor:pointer;font:inherit}
.step .num{grid-row:1/3;width:24px;height:24px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;font:400 12px/1 var(--f-mono);color:var(--mut)}
.step.is-active .num,.step.is-done .num{border-color:var(--seal);color:var(--seal)}
.step.is-active .num{background:var(--seal);color:var(--on-seal);box-shadow:0 0 12px rgba(var(--seal-rgb),.45)}
.st-l{font-weight:600;font-size:14px;display:flex;align-items:center;flex-wrap:wrap}
.st-t{font-size:13.5px;color:var(--mut);line-height:1.45}
.more-btn{margin:0 0 6px 44px;background:none;border:0;padding:0;color:var(--seal);font:400 12.5px/1 var(--f-mono);letter-spacing:.04em;cursor:pointer}
.more{display:grid;grid-template-rows:0fr;transition:grid-template-rows var(--dur) var(--ease)}
.more>div{overflow:hidden;min-height:0}
.more p{padding:0 10px 10px 44px;font-size:13.5px;color:var(--mut)}
.more-btn[aria-expanded="true"]+.more{grid-template-rows:1fr}
html:not(.js) .more{grid-template-rows:1fr}
.textv{grid-column:1/-1;font-size:14px;color:var(--mut)}
.textv summary{cursor:pointer;color:var(--seal);font-family:var(--f-mono);font-size:12.5px;letter-spacing:.06em;text-transform:uppercase}
.textv ol{margin:8px 0 0;padding-left:20px}
.textv strong{color:var(--ink)}
@media(max-width:960px){.dg{grid-template-columns:minmax(0,1fr)}}
@media(max-width:720px){.dg-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}.dg-svg{min-width:680px}}

/* diagram states */
.dg .st{--o:.32;--dim:1;opacity:calc(var(--o)*var(--dim));transition:opacity var(--dur) var(--ease)}
.dg .st.on{--o:.62}
.dg .st.active{--o:1}
html:not(.js) .dg .st{--o:1}
.dg[data-path="allow"] .br:not(.br-allow),.dg[data-path="escalate"] .br:not(.br-escalate),.dg[data-path="deny"] .br:not(.br-deny){--dim:.28}
.dg[data-path="allow"] .n5 .packet{stroke:var(--allow)}
.dg[data-path="escalate"] .n5 .packet{stroke:var(--esc)}
.dg[data-path="deny"] .n5 .packet{stroke:var(--deny);stroke-dasharray:6 6}
.dg[data-path="deny"] .n5 .stub,.dg[data-path="deny"] .n5 .stubt{opacity:.6}
.dg-svg text{fill:var(--ink);font-size:13px}
.dg-svg .lbl{font-size:13px}
.dg-svg .lbl.big{font-size:14px;font-weight:600}
.dg-svg .lbl.mono{font-family:var(--f-mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;fill:var(--mut)}
.dg-svg .lbl.dim{fill:var(--faint)}
.dg-svg .con{fill:none;stroke:var(--mut);stroke-width:2;stroke-linecap:round;stroke-dasharray:var(--len,none);stroke-dashoffset:var(--len,0);transition:stroke-dashoffset var(--dur-slow) var(--ease)}
.dg-svg marker path{fill:var(--mut)}
.dg .st.on .con,.dg .st.active .con{stroke-dashoffset:0}
.dg-svg .con.flow{stroke:var(--seal-hi);stroke-dasharray:7 11;stroke-dashoffset:0;opacity:0}
.dg .st.active .con.flow{opacity:1;animation:dash 1s linear infinite}
@keyframes dash{to{stroke-dashoffset:-36}}
.dg-svg .hex{fill:var(--card);stroke:var(--mut);stroke-width:2}
.dg .n1.on .hex,.dg .n1.active .hex{stroke:var(--seal);fill:var(--seal-soft)}
.dg-svg .ring{fill:none;stroke:var(--deny-hi);stroke-width:2;opacity:0}
.dg-svg .sb circle{fill:var(--panel2);stroke:var(--line);stroke-width:1.5}
.dg-svg .sb text{font-family:var(--f-mono);font-size:12px;fill:var(--mut)}
.dg .st.active .sb circle{fill:var(--seal);stroke:var(--seal);filter:drop-shadow(0 0 6px rgba(var(--seal-rgb),.6))}
.dg .st.active .sb text{fill:var(--on-seal);font-weight:600}
.dg .st.on .sb circle{stroke:var(--seal)}
.dg .st.on .sb text{fill:var(--seal)}
.dg-svg .owner{fill:var(--card);stroke:var(--mut);stroke-width:2}
.dg .n2.on .owner,.dg .n2.active .owner{stroke:var(--seal)}
.dg-svg .tickc{fill:var(--seal);stroke:none}
.dg-svg .tickp{fill:none;stroke:var(--on-seal);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.dg-svg .frame{fill:none;stroke:var(--seal);stroke-width:1.5;stroke-dasharray:6 6;opacity:.9}
.dg-svg .oof{opacity:0}
.dg-svg .oof rect{fill:var(--deny);stroke:none}
.dg-svg .oof path{stroke:var(--on-seal);stroke-width:2;stroke-linecap:round}
.dg .n3.active .oof{animation:oof 1.5s var(--ease) 1 forwards}
@keyframes oof{0%{opacity:0;transform:translateY(-6px)}25%{opacity:1;transform:none}60%{opacity:1;transform:none}100%{opacity:0;transform:translateY(26px)}}
.dg-svg .gate .post{fill:var(--line)}
.dg-svg .gate .door{fill:var(--card);stroke:var(--mut);stroke-width:1.5}
.dg .n4.on .gate .door,.dg .n4.active .gate .door{fill:var(--seal-soft);stroke:var(--seal)}
.dg.done .n4 .gate .door{animation:breathe 3.2s ease-in-out infinite}
@keyframes breathe{0%,100%{fill:var(--seal-soft)}50%{fill:var(--seal-soft2)}}
.dg-svg .pill rect{fill:var(--card);stroke:var(--line);stroke-width:1.5}
.dg-svg .pill text{font-family:var(--f-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase}
.dg-svg .p-allow rect{stroke:var(--allow)} .dg-svg .p-allow text{fill:var(--allow-hi)}
.dg-svg .p-esc rect{stroke:var(--esc)} .dg-svg .p-esc text{fill:var(--esc-hi)}
.dg-svg .p-deny rect{stroke:var(--deny)} .dg-svg .p-deny text{fill:var(--deny-hi)}
.dg-svg .p-road rect{stroke:var(--roadmap)} .dg-svg .p-road text{fill:var(--roadmap)}
.dg-svg .packet{fill:var(--card);stroke:var(--mut);stroke-width:2}
.dg-svg .seal circle{fill:var(--seal);transform-box:fill-box;transform-origin:center}
.dg .n5.active .seal{animation:pop 1.2s var(--ease) 1}
@keyframes pop{0%{transform:scale(.2);opacity:0}45%{transform:scale(1.18);opacity:1}100%{transform:scale(1);opacity:1}}
.dg-svg .stub{fill:var(--panel2);stroke:var(--line)}
.dg-svg .stubt{fill:var(--seal)}
.dg-svg .org{fill:var(--card);stroke:var(--line);stroke-width:1.5}
.dg-svg .strip{fill:var(--panel2);stroke:var(--line)}
.dg-svg .cell{fill:var(--hair);transition:fill .3s var(--ease);transition-delay:calc(var(--i)*110ms)}
.dg .n6.on .cell,.dg .n6.active .cell{fill:var(--seal)}
.dg-svg .radar{fill:none;stroke:var(--line);stroke-width:1.5}
.dg-svg .radar2{fill:none;stroke:var(--hair)}
.dg-svg .sweep line{stroke:var(--seal-hi);stroke-width:2;stroke-linecap:round}
.dg-svg .sweep{opacity:0;transform-box:view-box}
.dg .n6.active .sweep{opacity:1;animation:sweep 1.6s linear 1 forwards}
@keyframes sweep{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
.dg-svg .anom{fill:var(--deny-hi);opacity:0}
.dg .n6.active .anom{animation:anom .6s ease-out 1.1s 1 forwards}
@keyframes anom{to{opacity:1}}
.dg-svg .kill{fill:none;stroke:var(--deny-hi);stroke-width:3;stroke-linecap:round;stroke-dasharray:var(--len,none);stroke-dashoffset:var(--len,0);opacity:0}
.dg .n6.active .kill,.dg .n4.active .kill{opacity:.9;animation:killdraw .4s ease-out .9s 1 forwards}
.dg .n6.active .ring{animation:ring .4s ease-out 1.1s 1 forwards}
@keyframes killdraw{to{stroke-dashoffset:0}}
@keyframes ring{to{opacity:.9}}
.dg-svg .killt{fill:var(--deny-hi);opacity:0}
.dg .n6.active .killt,.dg .n4.active .killt{opacity:1;transition:opacity .3s 1.2s}
.dg-svg .boundary{fill:none;stroke:var(--seal);stroke-width:1.5;stroke-dasharray:6 6;opacity:.7}
.dg-svg .row{fill:var(--card);stroke:var(--line)}
.dg-svg .panelr{fill:var(--card);stroke:var(--line)}
.dg-svg .q1,.dg-svg .q2{fill:var(--ink);text-transform:none;letter-spacing:0;opacity:0}
.dg .n5.active .q1,.dg .n5.on .q1{opacity:1;transition:opacity .3s .2s}
.dg .n5.active .q2,.dg .n5.on .q2{opacity:1;transition:opacity .3s .7s}
.dg.done .n6.active .kill{opacity:.45}
.dg.done .n6.active .killt{opacity:.7}
.dg-svg .roadbox{fill:none;stroke:var(--roadmap);stroke-dasharray:5 6}
.dg-svg .bit{transform-box:fill-box;transform-origin:center}
.dg .n3.active .bit{animation:travel 1.2s var(--ease) 1 forwards}
@keyframes travel{from{transform:translateX(0)}to{transform:translateX(50px)}}
.dg-svg .node{cursor:default;outline:none}
.dg-svg .node:focus-visible .sb circle{stroke:var(--ink)}

/* tooltip */
.tip{position:fixed;z-index:60;max-width:280px;padding:10px 12px;border-radius:10px;background:var(--tipbg);border:1px solid var(--line);color:var(--ink);font-size:13px;line-height:1.5;box-shadow:var(--shadow);pointer-events:none;opacity:0;transition:opacity var(--dur-fast)}
.tip.is-on{opacity:1}

/* architecture strip */
.arch{padding:24px 0}
.arch details{border:1px solid var(--line);border-radius:var(--radius);background:var(--panel)}
.arch summary{padding:16px 20px;cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between}
.arch summary::-webkit-details-marker{display:none}
.arch summary::after{content:"+";font-family:var(--f-mono);color:var(--seal)}
.arch details[open] summary::after{content:"–"}
.arch .arch-svg{width:100%;height:auto;display:block;padding:0 12px 12px}
.arch .arch-svg text{fill:var(--ink);font-size:13px}
.arch .arch-svg .lbl.mono{font-family:var(--f-mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;fill:var(--mut)}
.arch .arch-svg .lbl.big{font-weight:600}
.arch .arch-svg .con{fill:none;stroke:var(--mut);stroke-width:2}
.arch .arch-svg marker path{fill:var(--mut)}
.arch .arch-svg .org,.arch .arch-svg .packet,.arch .arch-svg .strip{fill:var(--card);stroke:var(--line);stroke-width:1.5}
.arch .arch-svg .gate .post{fill:var(--line)}
.arch .arch-svg .gate .door{fill:var(--seal-soft);stroke:var(--seal);stroke-width:1.5}

/* closing */
.close{padding:56px 0}
.close .box{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:20px;padding:28px;border-radius:var(--radius);background:var(--seal-soft);border:1px solid rgba(var(--seal-rgb),.3)}
.close h2{font:600 clamp(20px,2.4vw,26px)/1.25 var(--f-head)}
.close .contact{margin-top:14px;color:var(--mut);font-size:14.5px}
.close .stand{margin-top:6px}
.qrbox{display:flex;flex-direction:column;gap:10px;align-items:flex-start}
.qr{border-radius:10px;display:block}
.qrbox .cap{font-size:13.5px;color:var(--mut)}
.qrbox a{word-break:break-all;font-family:var(--f-mono);font-size:12px}
@media(max-width:960px){.close .box{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.close .box{grid-template-columns:1fr}}
footer{padding:24px 0 48px;border-top:1px solid var(--hair);color:var(--faint);font-size:13px}
footer .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:16px}
footer .brand img.wm{height:10px;opacity:.85;filter:invert(var(--logo-invert))}
footer a{color:var(--mut)}
footer .grow{flex:1}

@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .dg *,.drawer-body,.more,.ind,.panel,.tab-cta,.btn,.chip{animation:none!important;transition:none!important}
  .dg-svg .con{stroke-dashoffset:0!important}
  .dg-svg .oof,.dg-svg .sweep,.dg-svg .anom,.dg-svg .kill,.dg-svg .killt,.dg-svg .ring{opacity:1!important;stroke-dashoffset:0!important}
}
@media print{
  html.js .panel{display:block!important}
  .panel{page-break-before:always;border:0}
  .top,.tabs,.dg-ctl,.more-btn,.drawer-btn::after,.skip,.tip,.close .btn{display:none!important}
  .drawer-body,.more{grid-template-rows:1fr!important}
  body{background:#fff;color:#000}
  .dg .st{--o:1!important}
  .card,.drawer,.tab-cta,.close .box{border-color:#999;background:#fff}
  .dg-svg text{fill:#000}
}
"""

# ---------------------------------------------------------------- JS
JS = r"""
(function(){
  var d=document, root=d.documentElement; root.classList.add('js');
  /* theme: light by default, dark by toggle (remembered per device) */
  var th=null; try{ th=localStorage.getItem('riyadh-theme'); }catch(e){}
  if(th==='dark') root.setAttribute('data-theme','dark');
  d.querySelectorAll('.theme').forEach(function(b){ b.addEventListener('click', function(){ var dark=root.getAttribute('data-theme')==='dark'; if(dark) root.removeAttribute('data-theme'); else root.setAttribute('data-theme','dark'); try{ localStorage.setItem('riyadh-theme', dark?'light':'dark'); }catch(e){} }); });
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var STEPS=6, DWELL=1600;

  /* ---------- diagram controller ---------- */
  function Diagram(fig){
    this.fig=fig; this.i=0; this.timer=null; this.playing=false;
    this.pos=fig.querySelector('.dg-pos'); this.play=fig.querySelector('.play'); this.list=fig.querySelectorAll('.step');
    var self=this;
    fig.querySelectorAll('path.con, path.kill').forEach(function(p){ try{ var L=p.getTotalLength(); p.style.setProperty('--len', L.toFixed(1)); }catch(e){} });
    this.play.addEventListener('click', function(){ self.playing ? self.pause() : self.start(); });
    fig.querySelector('.restart').addEventListener('click', function(){ self.restart(); });
    this.list.forEach(function(li){
      li.querySelector('.step-btn').addEventListener('click', function(){ self.pause(); self.set(+li.dataset.i); });
      var mb=li.querySelector('.more-btn');
      mb.addEventListener('click', function(){ var o=mb.getAttribute('aria-expanded')==='true'; mb.setAttribute('aria-expanded', o?'false':'true'); });
    });
    this.set(0);
  }
  Diagram.prototype.set=function(i){
    var fig=this.fig; this.i=i; fig.dataset.step=i;
    fig.querySelectorAll('[data-s]').forEach(function(el){ var s=+el.dataset.s; el.classList.toggle('on', s<i); el.classList.toggle('active', s===i); });
    fig.classList.toggle('done', i===STEPS);
    this.list.forEach(function(li){ var s=+li.dataset.i; li.classList.toggle('is-active', s===i); li.classList.toggle('is-done', s<i); li.querySelector('.step-btn').setAttribute('aria-current', s===i?'step':'false'); });
    this.pos.textContent='Step '+i+' of '+STEPS;
  };
  Diagram.prototype.tick=function(){ if(this.i<STEPS){ this.set(this.i+1); if(this.i===STEPS){ this.pause(); } } };
  Diagram.prototype.start=function(){ if(this.i>=STEPS) this.set(0); this.playing=true; this.play.textContent='Pause'; this.play.setAttribute('aria-pressed','true'); var self=this; clearInterval(this.timer); this.tick(); this.timer=setInterval(function(){ self.tick(); }, DWELL); };
  Diagram.prototype.pause=function(){ this.playing=false; clearInterval(this.timer); this.play.textContent='Play'; this.play.setAttribute('aria-pressed','false'); };
  Diagram.prototype.restart=function(){ this.pause(); this.set(0); if(reduce){ this.set(STEPS); } else { this.start(); } };
  Diagram.prototype.show=function(){ if(reduce){ this.pause(); this.set(STEPS); return; } var self=this; this.pause(); this.set(0); setTimeout(function(){ if(self.fig.closest('.panel').classList.contains('is-active')) self.start(); }, 350); };

  var diagrams={};
  d.querySelectorAll('.panel').forEach(function(p){ diagrams[p.id]=new Diagram(p.querySelector('.dg')); });

  /* ---------- chips ---------- */
  d.querySelectorAll('.panel').forEach(function(p){
    var fig=p.querySelector('.dg'), sc=p.querySelector('.scenario-t'), pk=fig.querySelector('#pk-'+p.id);
    p.querySelectorAll('.chip').forEach(function(c){
      c.addEventListener('click', function(){
        p.querySelectorAll('.chip').forEach(function(x){ x.classList.remove('is-on'); x.setAttribute('aria-checked','false'); });
        c.classList.add('is-on'); c.setAttribute('aria-checked','true');
        sc.textContent=c.dataset.scenario;
        if(c.dataset.path){ fig.dataset.path=c.dataset.path; }
        if(pk && c.dataset.packet){ pk.textContent=c.dataset.packet; }
        var dg=diagrams[p.id];
        if(c.dataset.focus){ dg.pause(); dg.set(+c.dataset.focus); } else { dg.restart(); }
      });
    });
  });

  /* ---------- drawers ---------- */
  d.querySelectorAll('.drawer-btn').forEach(function(b){ b.addEventListener('click', function(){ var o=b.getAttribute('aria-expanded')==='true'; b.setAttribute('aria-expanded', o?'false':'true'); }); });

  /* ---------- tabs ---------- */
  var tabs=Array.prototype.slice.call(d.querySelectorAll('.tab')), panels=Array.prototype.slice.call(d.querySelectorAll('.panel')), ind=d.querySelector('.ind'), list=d.querySelector('.tablist');
  function moveInd(tab){ ind.style.left=(tab.offsetLeft - list.scrollLeft)+'px'; ind.style.width=tab.offsetWidth+'px'; }
  function select(id, focus, push){
    var tab=d.getElementById('tab-'+id); if(!tab) return;
    tabs.forEach(function(t){ var on=t===tab; t.setAttribute('aria-selected', on?'true':'false'); t.tabIndex=on?0:-1; });
    panels.forEach(function(p){ var on=p.id===id; p.classList.toggle('is-active', on); if(!on && diagrams[p.id]) diagrams[p.id].pause(); });
    moveInd(tab);
    var L=tab.offsetLeft-16, R=tab.offsetLeft+tab.offsetWidth+16-list.clientWidth; if(list.scrollLeft>L) list.scrollLeft=L; else if(list.scrollLeft<R) list.scrollLeft=R;
    if(diagrams[id]) diagrams[id].show();
    if(push && location.hash!=='#'+id){ history.pushState(null,'','#'+id); }
    if(focus) tab.focus();
  }
  tabs.forEach(function(t,i){
    t.addEventListener('click', function(){ select(t.dataset.id, false, true); window.scrollTo({top: d.querySelector('.tabs').offsetTop - 56, behavior: reduce?'auto':'smooth'}); });
    t.addEventListener('keydown', function(e){
      var k=e.key, j=i;
      if(k==='ArrowRight') j=(i+1)%tabs.length; else if(k==='ArrowLeft') j=(i-1+tabs.length)%tabs.length; else if(k==='Home') j=0; else if(k==='End') j=tabs.length-1; else return;
      e.preventDefault(); select(tabs[j].dataset.id, true, true);
    });
  });
  function fromHash(){ var id=(location.hash||'#banks').slice(1); if(!d.getElementById('tab-'+id)) id='banks'; select(id,false,false); }
  window.addEventListener('hashchange', fromHash);
  window.addEventListener('resize', function(){ var t=d.querySelector('.tab[aria-selected="true"]'); if(t) moveInd(t); });
  list.addEventListener('scroll', function(){ var t=d.querySelector('.tab[aria-selected="true"]'); if(t) moveInd(t); });
  d.querySelectorAll('.seg-chips a').forEach(function(a){ a.addEventListener('click', function(e){ e.preventDefault(); select(a.getAttribute('href').slice(1), false, true); d.querySelector('.tabs').scrollIntoView({behavior: reduce?'auto':'smooth'}); }); });
  fromHash();

  /* ---------- tooltips ---------- */
  var tip=d.createElement('div'); tip.className='tip'; tip.setAttribute('role','tooltip'); d.body.appendChild(tip);
  function showTip(el){ tip.textContent=el.dataset.tip; var r=el.getBoundingClientRect(); tip.classList.add('is-on'); var x=Math.min(Math.max(8, r.left), window.innerWidth-tip.offsetWidth-8), y=r.top-tip.offsetHeight-8; if(y<8) y=r.bottom+8; tip.style.left=x+'px'; tip.style.top=y+'px'; }
  function hideTip(){ tip.classList.remove('is-on'); }
  d.querySelectorAll('[data-tip]').forEach(function(el){
    el.addEventListener('mouseenter', function(){ showTip(el); }); el.addEventListener('mouseleave', hideTip);
    el.addEventListener('focus', function(){ showTip(el); }); el.addEventListener('blur', hideTip);
    el.addEventListener('touchstart', function(){ showTip(el); setTimeout(hideTip, 2500); }, {passive:true});
  });
  d.addEventListener('keydown', function(e){ if(e.key==='Escape') hideTip(); });
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(function(){ var t=d.querySelector('.tab[aria-selected="true"]'); if(t) moveInd(t); }); }
})();
"""

# ---------------------------------------------------------------- page
def build():
    tabs = "".join(f'<button class="tab" role="tab" id="tab-{s["id"]}" data-id="{s["id"]}" aria-selected="{"true" if i == 0 else "false"}" aria-controls="{s["id"]}" tabindex="{0 if i == 0 else -1}">{esc(s["label"])}</button>' for i, s in enumerate(SEGMENTS))
    seg_chips = "".join(f'<a href="#{s["id"]}"><span class="mono">0{i+1}</span>{esc(s["label"])}</a>' for i, s in enumerate(SEGMENTS))
    panels = "".join(render_segment(s) for s in SEGMENTS)
    css = CSS.replace("%ORBITRON%", b64("Orbitron-600.woff2")).replace("%OXANIUM%", b64("Oxanium-400.woff2")).replace("%GEISTMONO%", b64("GeistMono-400.woff2"))
    wm = "data:image/png;base64," + b64("wordmark-white-crop.png")
    ic = "data:image/png;base64," + b64("icon-white-crop.png")
    loud = esc(POSITIONING["loud"]).replace("before it moves", "<em>before it moves</em>")
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Regent Protocol · {esc(EVENT["name"])}</title>
<meta name="description" content="{attr(POSITIONING["kicker"] + " " + POSITIONING["loud"])}">
<link rel="icon" href="{ic}">
<style>{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{attr(CTA["site"])}" aria-label="Regent Protocol"><img class="ic" src="{ic}" alt="" width="22" height="21"><img class="wm" src="{wm}" alt="Regent Protocol"></a>
    <span class="badge">{esc(EVENT["badge"])}</span>
    <span class="grow"></span>
    <span class="lang" aria-label="Language">EN</span>
    <button type="button" class="btn theme" aria-label="Switch colour theme"><span class="l">Dark</span><span class="d">Light</span></button>
    <a class="btn primary" href="{attr(CTA["url"])}" target="_blank" rel="noopener">{esc(CTA["label"])}</a>
  </div>
</header>
<main id="main">
  <section class="hero"><div class="wrap">
    <h1><span class="k">{esc(POSITIONING["kicker"])}</span><span class="loud">{loud}</span></h1>
    <p class="lead">Pick your segment. Each tab shows the same decision, told for your organisation, with the technical depth one tap away.</p>
    <nav class="seg-chips" aria-label="Segments">{seg_chips}</nav>
  </div></section>
  {render_numbers()}
  <nav class="tabs" aria-label="Segments">
    <div class="wrap"><div class="tablist" role="tablist" aria-label="Audience segments">{tabs}</div><span class="ind" aria-hidden="true"></span></div>
  </nav>
  <div class="panels">{panels}</div>
  <section class="arch"><div class="wrap">
    <details><summary><span>One decision layer for all four segments</span></summary>{svg_arch()}</details>
  </div></section>
  <section class="close"><div class="wrap"><div class="box">
    <div>
      <h2>{esc(CTA["closing"])}</h2>
      <p class="contact">{esc(CTA["contact_line"])}</p>
      <p class="contact stand">{esc(EVENT["stand"])} · {esc(EVENT["dates"])}</p>
      <p style="margin-top:18px"><a class="btn primary" href="{attr(CTA["url"])}" target="_blank" rel="noopener">{esc(CTA["label"])}</a></p>
    </div>
    <div class="qrbox">{qr_svg("QR_WA", 148)}<span class="cap">Scan to open WhatsApp with Sayat.</span></div>
    <div class="qrbox">{qr_svg("QR_RECEIPT", 148)}<span class="cap">Verify a real receipt from get4agent.com against our public keys.</span><a href="{attr(CTA["receipt_url"])}" target="_blank" rel="noopener">{esc(CTA["receipt_label"])}</a></div>
  </div></div></section>
</main>
<footer><div class="wrap">
  <a class="brand" href="{attr(CTA["site"])}"><img class="wm" src="{wm}" alt="Regent Protocol"></a>
  <span>© Regent Protocol 2026</span>
  <span class="grow"></span>
  <a href="{attr(CTA["site"])}">regentprotocol.org</a>
  <a href="{attr(CTA["tour"])}">How it works</a>
</div></footer>
<script>{JS}</script>
</body>
</html>'''
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    write_copy_deck()
    scan(page, out)

def write_copy_deck():
    L = ["# Copy deck · Regent Protocol · Money20/20 Riyadh 2026", "", "Every English string on the page, in page order. Source of truth: `data.py`.", ""]
    L += ["## Top bar", f"- Wordmark: Regent Protocol", f"- Badge: {EVENT['badge']}", f"- CTA: {CTA['label']} → {CTA['url']}", ""]
    L += ["## Hero", f"- {POSITIONING['kicker']}", f"- {POSITIONING['loud']}", "- Pick your segment. Each tab shows the same decision, told for your organisation, with the technical depth one tap away.", ""]
    L += ["## In production", f"- {NUMBERS['as_of']}"] + [f"- {x['n']} · {x['label']} · {x['note']}" for x in NUMBERS["items"]] + [f"- {NUMBERS['bench']}", ""]
    for s in SEGMENTS:
        L += [f"## Tab · {s['label']} (#{s['id']})", f"- Promise: {s['promise']}", "- Sub-chips and scenarios:"]
        L += [f"  - {c['name']}: {c['scenario']}" for c in s["chips"]]
        L += ["- Why it matters:"] + [f"  - {w['h']}: {w['p']}" for w in s["why"]]
        L += ["- Diagram steps:"] + [f"  {i}. {st['label']}: {st['text']}  (learn more: {st['more']}){'  [Roadmap: ' + st['roadmap'] + ']' if st.get('roadmap') else ''}" for i, st in enumerate(s["steps"], 1)]
        L += ["- What this gives you:"] + [f"  - {g['dim']}: {g['h']}. {g['p']}" for g in s["gives"]]
        L += [f"- Before: {s['before']}", f"- After: {s['after']}"]
        if s.get("subcase"):
            L += [f"- Sub-case ({s['subcase']['h']}): {s['subcase']['p']}"]
        L += ["- Learn more drawer:"]
        for sec in s["drawer"]:
            L += [f"  - {sec['h']}"] + [f"    - {(it['text'] + ' [Roadmap]') if isinstance(it, dict) else it}" for it in sec["items"]]
        L += [f"- Tab CTA: {CTA['closing']} / {CTA['label']}", ""]
    L += ["## Architecture strip", "- One decision layer for all four segments", ""]
    L += ["## Closing", f"- {CTA['closing']}", f"- {CTA['contact_line']}", f"- {EVENT['stand']} · {EVENT['dates']}", "- Scan to open WhatsApp with Sayat.", f"- Verify a real receipt from get4agent.com against our public keys. {CTA['receipt_url']}", ""]
    L += ["## Footer", "- © Regent Protocol 2026 · regentprotocol.org · How it works", ""]
    with open(os.path.join(HERE, "copy-deck.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))

BANNED = [(r"\bKYA\b", 0), (r"know your agent", re.I), (r"\bDeFi\b", 0), (r"crypto", re.I), (r"token price", re.I), (r"\byield\b", re.I), (r"\blending\b", re.I), (r"deepfake", re.I)]

def scan(page, out):
    text = re.sub(r"<style>.*?</style>", "", page, flags=re.S)
    text = re.sub(r"<script>.*?</script>", "", text, flags=re.S)
    text = re.sub(r'data:[^"\']+', "", text)
    hits = []
    for pat, fl in BANNED:
        for m in re.finditer(pat, text, fl):
            hits.append((pat, text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    size = os.path.getsize(out)
    print(f"wrote {out}  ({size/1024:.1f} KB)")
    ext = re.findall(r'(?:src|href)="(https?://[^"]+)"', page)
    print("external references (links only, no loads):", sorted(set(ext)))
    if hits:
        print("BANNED STRINGS FOUND:")
        for h in hits:
            print("  ", h)
        sys.exit(1)
    print("banned-string scan: clean")

if __name__ == "__main__":
    build()
