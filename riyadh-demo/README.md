# Regent Protocol · Money20/20 Riyadh 2026 · segment demo page

One self-contained page for the stand: four audience tabs, one animated decision map per tab, technical depth behind "Learn more".

## Files

- `../v2-static/riyadh/index.html` — the page. Single file, inline CSS/JS, inline fonts, inline logo, inline QR codes. **No network requests at runtime.**
- `data.py` — every string on the page (copy, scenarios, steps, drawers, numbers, CTA). Edit here.
- `build.py` — assembles the page from `data.py` + `assets/`, writes `copy-deck.md`, scans for banned strings, prints the size.
- `copy-deck.md` — generated; all English strings in page order, for review.
- `assets/` — subsetted OFL fonts (Orbitron 600, Oxanium variable, Geist Mono 400), the Regent logo as white-on-transparent PNG, `qr.json` (pre-rendered QR paths).
- `riyadh-page-qr.png` — QR code for `https://regentprotocol.org/riyadh`, for print.

## Open the page offline

Copy `index.html` to the tablet or laptop and open it in Chrome, Safari or Edge (double-click, or drag into the browser). Everything is inside the file. Deep links work locally too: `index.html#banks`, `#commerce`, `#regulators`, `#stablecoin`.

Online copy: `https://regentprotocol.org/riyadh` (same file, served by nginx from `/opt/regent-v2/riyadh/`).

## Edit copy or numbers

1. Change `data.py` (word budgets from the brief: promise ≤14 words, why-card ≤18, value card ≤20, step label ≤5, step sentence ≤16, before/after ≤25).
2. Run `python3 build.py` (Python 3, no dependencies).
3. The build fails if any banned string appears in visible text: `KYA`, `Know Your Agent`, `DeFi`, `crypto`, `token price`, `yield`, `lending`, `deepfake`.
4. Re-copy `index.html` to the devices.

Anything not shipped must carry a `Roadmap` chip. In `data.py`: a step gets `"roadmap": "…"`, a drawer item becomes `{"text": "…", "roadmap": True}`.

## Themes and brand tokens

The page ships two themes from the site's palette. **Light is the default** (paper `#F7F7F3`, seal `#007A6E`, ink `#16211E`); **dark** (`#0F1513` base, seal `#00C9B7`) is one tap away on the "Dark / Light" button in the top bar and is remembered per device in `localStorage`. All colours, radii and durations are CSS custom properties at the top of `build.py` (`CSS` block): `:root` holds the light set, `:root[data-theme="dark"]` the dark set; the neutral ramp and the three outcome colours (`--allow`, `--esc`, `--deny`) come from the live site and the `/how-it-works` tour. The logo PNGs are white on transparent and are inverted by CSS on the light theme (`--logo-invert`). Fonts: replace the `.woff2` files in `assets/` and the `@font-face` lines.

## Segment data structure

Each entry in `SEGMENTS` (data.py):

- `id`, `label`, `variant` (`flow` for banks/commerce/stablecoin, `record` for regulators), `org` (label of the right-hand node), `promise`
- `chips`: `name`, `scenario`, and either `path` (`allow` / `escalate` / `deny`, lights that branch) + `packet` (label on the transaction), or `focus` (step number to jump to, record variant)
- `why` (3 cards), `steps` (6: `label`, `text`, `more`, optional `roadmap`), `gives` (4: Revenue / Cost / Risk / Speed), `before`, `after`, optional `subcase`, `drawer` (sections with items)

## Resolved `[CONFIRM]` items (11 September 2026)

1. Meeting CTA: WhatsApp Sayat Kakzhanov +7 700 157 1111 (`https://wa.me/77001571111`). Stand H2.P124, Startup Pod, 14–16 September.
2. Numbers shown are production counts read on 11 September 2026 (data through 9 September): 556 gate decisions, 925/925 audit events anchored in 112 batches (Solana devnet), 67 AgentIDs (36 active, 31 revoked), 41 active mandates, 12 signed receipts on get4agent.com. Benchmarks from 27 August 2026: authorize ~0.5 s, kill switch to first refusal 0.43–0.49 s, batch anchored ~2 s after sealing. Re-read before reuse.
3. Integration surface: the routes in the Banks drawer are the documented org-scoped routes (`/v1/organizations/{org}/mandates/{id}/authorize`, `…/audit/events/{id}` + `/verify`, `…/agents/{id}/revoke`), JWKS at `/.well-known/jwks.json`, Cloud Gateway and sidecar per docs.regentprotocol.org.
4. Roadmap chips shown: aggregate supervision views and reporting; KYB verification flow; sanctions screening as a gate input; named abuse patterns and quantity/velocity rules; on-chain enforcement program.
5. Authority access is worded as a legal-basis question, never as a feature; no regulator is named.
6. Brand kit: real logo (PNG, white on transparent) and site tokens; no separate SVG wordmark exists.
7. Font licences: Orbitron, Oxanium and Geist Mono are SIL Open Font License 1.1, embedding permitted.
8. Compliance sign-off on the Regulators and Stablecoin tabs: Sayat.

## QA done on 11 September

Headless Chrome with mobile emulation: 390 px wide page has no horizontal overflow (tabs and the diagram scroll inside their own containers); no console errors; banned-string scan clean; size about 200 KB including fonts; works with JavaScript disabled (tabs stack, drawers open); `prefers-reduced-motion` shows every diagram in its final state without autoplay.
