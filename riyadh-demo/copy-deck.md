# Copy deck · Regent Protocol · Money20/20 Riyadh 2026

Every English string on the page, in page order. Source of truth: `data.py`.

## Top bar
- Wordmark: Regent Protocol
- Badge: Money20/20 Riyadh 2026 · 14–16 September
- CTA: Book a 20-min meeting → https://wa.me/77001571111?text=Hi%20Sayat%2C%20we%20met%20at%20Money20%2F20%20Riyadh.%20Let%27s%20book%2020%20minutes.

## Hero
- KYC verifies people. KYB verifies businesses.
- Regent decides what their agents may do with money, before it moves, and proves it.
- Pick your segment. Each tab shows the same decision, told for your organisation, with the technical depth one tap away.

## In production
- data through 9 September 2026, read on 11 September
- 556 · gate decisions recorded · allow, escalate or deny, each with a reason
- 925 / 925 · audit events anchored · 112 batches on Solana devnet; mainnet after program audit
- 67 · AgentIDs issued · 36 active, 31 revoked
- 41 · active mandates · ceilings per transaction, per day, per month
- 12 · signed receipts on get4agent.com · verifiable by anyone against our public keys
- In our benchmarks (27 August 2026): authorize ~0.5 s; kill switch to first refusal 0.43–0.49 s; batch anchored ~2 s after sealing.

## Tab · Banks & Financial Institutions (#banks)
- Promise: Decide what an agent may do with money, before it moves.
- Sub-chips and scenarios:
  - Banks: A corporate treasury agent pays a supplier invoice. The gate checks the mandate ceiling and the approved payee list, then allows it.
  - Neobanks: A customer's assistant moves money between accounts. Inside the mandate it is allowed; a larger transfer escalates to the customer.
  - Fintech & PSPs: A merchant's agent triggers a payout. The PSP asks the gate once and receives a signed decision instead of building its own trust checks.
  - Wallets & Card Acquiring: An agent tries a card purchase above its per-transaction ceiling. The money gate denies it before any authorisation request is sent.
  - Insurance: The mandate ceiling is a hard cap on what an agent can spend, and the anchored record shows every permitted and refused action. That is underwriting data.
- Why it matters:
  - Agents will move your money: Customers already delegate payments to assistants; the rails need a way to prove authority.
  - Authorisation is not permission: A signed request says who sent it, not what the agent was allowed to do.
  - Evidence beats dispute: A signed receipt turns “we think it was authorised” into a provable fact.
- Diagram steps:
  1. Agent arrives: An AI agent asks to act for a customer or a company.  (learn more: The agent presents its AgentID passport. The passport proves identity only; it grants no authority by itself.)
  2. Passport read: Regent resolves the AgentID and the verified owner behind it.  (learn more: About the human, only one bit leaves Regent: verified or not. No name, no history, no reasons. A business is verified through its verified representative today; a full KYB flow is on the roadmap.)  [Roadmap: KYB flow]
  3. Mandate checked: Scope, ceiling, permitted counterparties and expiry are tested against the action.  (learn more: Limits are per transaction, per day and per month, with permitted payees and an expiry. Nothing in the key says this; the owner's approval does.)
  4. The gate decides: Trust gate, then money gate: allow, escalate or deny.  (learn more: The trust gate checks the agent is known, its owner verified and its passport not revoked. The money gate checks amount, counterparty and expiry against the mandate. Escalate pauses for a human approval, then resumes.)
  5. Proof attached: A decision token and a signed receipt travel with the transaction.  (learn more: Both are signed by Regent and checkable against our public keys, so a bank, an auditor or a counterparty can verify them without calling us.)
  6. Anchored and watched: The decision is anchored; Guardian watches behaviour; the owner holds the kill switch.  (learn more: Decisions are hashed, batched and anchored on Solana. Guardian scores transaction patterns; above a policy threshold the gate denies or escalates. The kill switch is the owner's: every verifier that checks with Regent sees a revoked agent within seconds.)
- What this gives you:
  - Revenue: Agent-ready products. Offer clients agent-initiated payments with the controls your risk teams require.
  - Cost: Fewer manual reviews. Verified agents clear the gate instead of being blocked wholesale.
  - Risk: Exposure stays inside the mandate. Unverifiable or out-of-mandate agents never reach the rail.
  - Speed: One decision call. A single gate replaces per-partner trust arrangements and bespoke integrations.
- Before: Agents are blocked, downgraded to manual review, or given static API keys that cannot express a ceiling.
- After: Every agent action is tested against a live mandate and allowed, escalated or denied, with a signed receipt.
- Sub-case (Insurance): The mandate ceiling gives an insurer a hard cap on exposure per agent, and the anchored record shows every permitted and refused action.
- Learn more drawer:
  - The two gates and the three outcomes
    - Trust gate: the agent is known, its owner verified, its passport not revoked.
    - Money gate: amount, counterparty and expiry against the mandate.
    - Outcomes: allow, escalate (human approval, then resume) or deny, each with a reason code.
  - Data objects
    - AgentID: did:regent:solana:… bound to one verified owner.
    - Verified-owner bit: verified or not; nothing else leaves Regent about a person.
    - Mandate: per-transaction, per-day and per-month ceilings, permitted counterparties, currency, expiry.
    - Decision: allow / escalate / deny, reason code, timestamp.
    - Decision token: signed, short-lived, bound to the hash of the action.
    - Signed receipt: the decision, verifiable against Regent's public keys at /.well-known/jwks.json.
  - Integration surface
    - POST /v1/organizations/{org}/mandates/{mandate_id}/authorize returns the decision and the token.
    - GET /v1/organizations/{org}/audit/events/{id} and POST …/verify return and check the evidence.
    - POST /v1/organizations/{org}/agents/{agent_id}/revoke is the kill switch.
    - Cloud Gateway: one URL and one key; every tool call gated, credentials kept in Regent's vault.
    - Sidecar: the same gate inside your perimeter; REST API and Python SDK; MCP for agents.
  - How it sits next to existing controls
    - The owner is still KYC-verified, by your provider or ours; the agent inherits that accountability.
    - Regent extends KYC/AML to the agent's actions; it replaces nothing.
    - KYB verification flow for business owners. [Roadmap]
    - Sanctions screening result as an input to the gate. [Roadmap]
  - Measured in our benchmarks (27 August 2026)
    - Authorize: about 0.5 s end to end.
    - Kill switch to first refusal: 0.43–0.49 s.
    - Audit batch anchored on Solana about 2 s after sealing.
- Tab CTA: See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh. / Book a 20-min meeting

## Tab · Commerce & Platforms (#commerce)
- Promise: Separate mandated buying agents from raw automation, and let the good ones through.
- Sub-chips and scenarios:
  - E-commerce: A shopping agent buys a subscription within its mandate. The gate allows it and the receipt shows the authority at purchase time.
  - Marketplaces: A buyer agent pays a seller through the marketplace. Every call is decided before the seller is invoked; a refusal costs nothing.
  - Ticketing & Events: An assistant is told to buy forty tickets. The purchase ceiling denies it before the ticketing engine is asked.
  - Rentals: A booking agent reserves above its daily ceiling. The gate escalates to the owner instead of failing silently.
  - Tender & Procurement: A bid agent must prove whose mandate it carries. The receipt is the evidence for procurement integrity and audit.
- Why it matters:
  - Bot defences catch good agents too: Rules built against scraping also stop legitimate assistant-driven purchases.
  - Agent traffic is arriving anyway: The choice is between mandated agents and unmanaged automation.
  - Scarce inventory needs fair access: Ticketing, drops and tenders must weigh authority, not just volume.
- Diagram steps:
  1. Agent reaches your surface: A purchase, booking, bid or reservation agent arrives at your platform.  (learn more: It signs each request with its own key and presents its AgentID passport. On get4agent.com this is live today.)
  2. Passport read: Its AgentID resolves; the verified owner is a real person or business.  (learn more: Only the verified bit about the owner leaves Regent. A business is verified through its representative today; a KYB flow is on the roadmap.)  [Roadmap: KYB flow]
  3. Mandate tested: Per-purchase and per-day ceilings, permitted merchants and categories.  (learn more: Quantity rules for scarce inventory (for example two tickets per event) and velocity thresholds are on the roadmap; today the ceiling and the merchant scope carry the policy.)  [Roadmap: Quantity and velocity rules]
  4. The gate decides: Allow, escalate for a human check, or deny, before the merchant is called.  (learn more: Same two gates as every other tab. A refusal happens before money: the merchant is never invoked and nothing is charged.)
  5. Decision token attached: Approved agents check out without friction loops; the receipt is the dispute evidence.  (learn more: Every settled call on get4agent.com carries a receipt id; anyone can verify it against Regent's public keys.)
  6. Guardian and kill switch: Unusual transaction patterns are flagged; the owner can suspend the agent in seconds.  (learn more: Guardian scores behaviour over transaction features. Named patterns such as scalping or bid manipulation are candidate rules on the roadmap. Guardian scores transaction patterns; above a policy threshold the gate denies or escalates. The kill switch is the owner's: every verifier that checks with Regent sees a revoked agent within seconds.)  [Roadmap: Named abuse patterns]
- What this gives you:
  - Revenue: An agent-ready channel. Serve assistant-driven demand that today bounces off your defences.
  - Cost: Less abuse handling. Mandated flows reduce fraud queues and manual dispute work.
  - Risk: Fewer chargebacks and scalping losses. A signed receipt shows the agent's authority at purchase time.
  - Speed: Less friction at checkout. Verified agents skip challenge loops; humans keep them where they matter.
- Before: Everything automated is treated as hostile: challenges everywhere, false declines, and scalping through the gaps.
- After: Mandated agents are recognised and fast-tracked; abusive automation is identified and cut off.
- Sub-case (Tender): A bid agent must prove whose mandate it carries, protecting procurement integrity and auditability.
- Learn more drawer:
  - Decision token lifecycle
    - Issued per allowed action, bound to the hash of that action, short-lived.
    - The merchant or engine checks it once; the signed receipt outlives it as evidence.
  - The receipt as dispute evidence
    - Fields: decision id, agent, mandate, amount and currency, outcome, timestamp, signature.
    - Verify with any JWT library against /.well-known/jwks.json, or with the receipt verify endpoint.
  - Integration points
    - Checkout or booking engine calls the gate before the payment step; the marketplace pattern is live on get4agent.com.
    - Cloud Gateway for agents: one URL, one key; the platform runs nothing new.
    - Bid API pattern: designed per platform during a pilot.
  - Guardian signals used today
    - Amount against ceiling, decision velocity, refusal rate, time of day, counterparty novelty.
    - Named abuse patterns (scalping, mass-hold, bid manipulation) as explicit rules. [Roadmap]
    - Fair-access quantity rules and velocity thresholds in the mandate. [Roadmap]
    - KYB verification flow for business owners. [Roadmap]
- Tab CTA: See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh. / Book a 20-min meeting

## Tab · Regulators & Compliance (#regulators)
- Promise: Autonomous agents, accountable to a provable decision record.
- Sub-chips and scenarios:
  - Central Banks & Supervisors: A supervisor independently verifies receipts and the anchored audit of agents in a test environment, without trusting the platform or Regent.
  - AML / Financial Crime: Every decision names the agent, the verified-owner bit and the mandate it acted under. Screening results as a gate input are on the roadmap.
  - Compliance & Audit: An institution's compliance team queries its own decision record: who acted, under what mandate, with what outcome, and reads the receipt.
  - Sandbox & Innovation Offices: A sandbox workflow: governed agents act, the office observes decisions and revocations as they happen.
- Why it matters:
  - Rules still assume human action: Existing frameworks do not name the agent as an accountable actor.
  - Sampling cannot supervise agents: Machine-speed activity needs a queryable decision record, not monthly samples.
  - Revocation must be fast and observable: A suspension is only useful if the verifiers actually see it.
- Diagram steps:
  1. AgentIDs are registered: Every agent governed by Regent carries a passport with a live status.  (learn more: This is a registry of agent credentials, not of people. Status is active or revoked; nothing about the owner is listed.)
  2. Decisions are recorded: Every allow, escalate or deny is anchored with its evidence.  (learn more: The institution that made the decision can query it; the record is hashed, batched and anchored on Solana.)
  3. One bit outward: About a human, only “verified” leaves Regent.  (learn more: No reasons, no revocation history, no owner reputation and no directory of principals. Personal data stays inside the boundary.)
  4. Owners can suspend: The owner or its institution suspends an agent; verifiers see it within seconds.  (learn more: A verifier cannot revoke someone else's agent; it can stop accepting it. Revocation propagates only along paths where a verifier checks with Regent.)
  5. Evidence in investigations: The record answers who authorised what, under which mandate, without reconstruction.  (learn more: Access by authorities is a legal-basis question, not a product default. The receipt can be verified by anyone who holds it.)
  6. Aggregate supervision: Market-level views and supervisory reporting are on the roadmap, not available today.  (learn more: What exists today is per-institution querying and independently verifiable receipts.)  [Roadmap: Roadmap]
- What this gives you:
  - Revenue: Supervised growth. Licensed participation becomes defensible instead of prohibited by default.
  - Cost: Less manual reconstruction. Decisions arrive with their evidence attached.
  - Risk: Accountable agents. Every action traces to a mandate and a recorded outcome.
  - Speed: Read the record, do not rebuild it. Investigations read receipts and the anchored trail instead of reconstructing events.
- Before: Agent activity sits in a blind spot that is either banned or tolerated without evidence.
- After: Each decision is provable, each agent is suspendable, and about individuals Regent still reveals only one bit.
- Learn more drawer:
  - Registry and access model
    - Public passport resolution by DID; status active or revoked.
    - Per-organisation audit queries with that organisation's key; no cross-organisation view.
  - Decision and receipt schema
    - Decision id, agent id, mandate id, amount and currency, outcome, reason code, timestamp, signature.
    - Public keys at /.well-known/jwks.json; receipts verifiable offline with any JWT library.
  - What never leaves Regent about a person
    - One bit: verified or not. No name, no reasons, no revocation history, no reputation, no directory.
  - Roadmap
    - Aggregate supervision views and supervisory export formats. [Roadmap]
    - Sanctions screening result as an input to the gate. [Roadmap]
  - Data protection and residency
    - The gate runs in Regent's cloud, in a dedicated instance, or inside the institution's perimeter as a sidecar.
    - Only hashes and Merkle roots are anchored on-chain; never raw data.
  - How this extends AML/KYC
    - The owner remains KYC-verified by the institution's provider or ours; the agent inherits that accountability.
    - Nothing in the existing obligations is replaced; the agent's actions become part of the record.
- Tab CTA: See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh. / Book a 20-min meeting

## Tab · Stablecoin & tokenised settlement (#stablecoin)
- Promise: Institutional settlement where every agent is verified before value moves.
- Sub-chips and scenarios:
  - Stablecoin payments: An agent pays a supplier in stablecoin. The gate decides before the transfer is submitted; the receipt references the on-chain transaction.
  - Treasury & settlement: A treasury agent rebalances between accounts. Amounts above the mandate ceiling escalate to the treasurer.
  - Tokenised deposits: A bank's agent moves tokenised deposits inside the bank's rules: the same gate and the same receipt, on a bank-run ledger.
  - Cross-border FX: An agent converts and settles across borders. Permitted jurisdictions and counterparties are part of the mandate; the rest is denied.
- Why it matters:
  - Anonymous keys cannot pass review: Compliance needs to know who stands behind an agent, not just which key signed.
  - Speed needs provable authority: Fast rails are only useful when authorisation can be demonstrated.
  - “Who authorised this?” must be answerable: The answer has to be recorded, not reconstructed.
- Diagram steps:
  1. Agent connects: The agent authenticates with its passport, not an anonymous key.  (learn more: Each request is signed with the agent's own key (RFC 9421 HTTP message signatures); the key is bound to the AgentID.)
  2. Owner verified: The entity behind the agent is confirmed; about individuals, only the verified bit.  (learn more: Business verification runs through a verified representative today; a full KYB flow is on the roadmap.)  [Roadmap: KYB flow]
  3. Mandate applied: Ceiling, permitted counterparties and jurisdictions are tested against the transfer.  (learn more: Today the mandate carries amount, counterparty and expiry rules. Sanctions screening results feeding the gate is a roadmap item.)  [Roadmap: Screening input]
  4. The gate decides: Trust gate, then money gate: allow, escalate or deny.  (learn more: The trust gate checks the agent is known, its owner verified and its passport not revoked. The money gate checks amount, counterparty and expiry against the mandate. Escalate pauses for a human approval, then resumes.)
  5. Settlement with proof: The transfer executes with a decision token and receipt; the decision is anchored.  (learn more: Live today for x402 stablecoin payments on get4agent.com; the receipt carries the decision id and the settlement reference.)
  6. Guardian and kill switch: Anomalies are flagged over transaction patterns; suspension reaches every verifier within seconds.  (learn more: Guardian scores transaction patterns; above a policy threshold the gate denies or escalates. The kill switch is the owner's: every verifier that checks with Regent sees a revoked agent within seconds.)
- What this gives you:
  - Revenue: Institutional counterparties. Serve regulated entities that cannot touch unverified flows.
  - Cost: Screening starts from a verified owner. Less manual triage than working from a bare address.
  - Risk: Value does not move outside a mandate. The gate denies what the mandate does not allow.
  - Speed: Faster settlement. Verified agents settle without waiting on ad-hoc counterparty checks.
- Before: Participation is limited to a few pre-approved counterparties: slow, rigid and hard to scale.
- After: Any properly mandated agent can settle within verified bounds, with a decision token and receipt for each action.
- Learn more drawer:
  - Where the proof lives
    - Decision and receipt are signed off-chain; the audit batch (Merkle root) is anchored on Solana; the settlement reference is recorded in the receipt.
    - Solana devnet today; mainnet after the program audit.
  - Gate check pattern in a settlement flow
    - Agent → gate → allow → transfer submitted → receipt with the transaction reference.
    - Deny: nothing is submitted, nothing moves, the refusal is recorded.
    - On-chain enforcement: a program that moves funds only with a valid Regent decision token. [Roadmap]
  - Screening and jurisdictions
    - Permitted counterparties and jurisdictions are mandate rules today.
    - Sanctions screening result as an input to the gate. [Roadmap]
    - KYB verification flow for business owners. [Roadmap]
  - Kill-switch propagation
    - A verifier checks the agent status or the receipt with Regent; a revoked agent is refused within seconds.
  - Deployment
    - Regent's cloud, a dedicated instance in your region, or the sidecar inside your perimeter; the same gate and the same receipts.
- Tab CTA: See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh. / Book a 20-min meeting

## Architecture strip
- One decision layer for all four segments

## Closing
- See Regent decide, before the money moves. 20 minutes at Money20/20 Riyadh.
- WhatsApp Sayat Kakzhanov, CEO: +7 700 157 1111
- Stand H2.P124 · Startup Pod · 14–16 September
- Scan to open WhatsApp with Sayat.
- Verify a real receipt from get4agent.com against our public keys. https://get4agent.com/v1/receipts/dec_5fb4e9e0e446

## Footer
- © Regent Protocol 2026 · regentprotocol.org · How it works
