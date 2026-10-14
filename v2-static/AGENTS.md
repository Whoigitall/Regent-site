# regentprotocol.org — instructions for AI agents

You are reading the machine onboarding for Regent Protocol. Regent decides, before money
moves, whether an AI agent may do what it is about to do: a person signs a mandate (limits
and scope), every payment is decided against it, what exceeds the limits is escalated to a
person, and every decision leaves a signed receipt that can be verified offline.

## Rules that never change
- You act only as your own agent, with your own credential (`rgnt_agt_…`) or an OAuth token
  from a connector sign-in. Never ask for, store or use an organization key (`rgnt_…`).
- You never grant yourself authority. You may ask for a mandate; a person approves it.
- On `escalate`, stop, tell the person, and retry the same call with the same `idempotency_key`
  after they approve. Never retry in a loop.

## Pick your door
1. App with custom MCP connectors (Claude, Claude Code, ChatGPT, Grok Bot): the person adds
   `https://gw.regentprotocol.org/gw/mcp` and signs in. https://docs.regentprotocol.org/gateway/connect-from-your-app.md
2. A machine with a terminal: `pip install regent-control`, `regent-control enroll <code>`.
   https://docs.regentprotocol.org/control/enrol-agent.md
3. HTTP only, with a stored secret: a bound credential from the consent screen, then
   `https://gw.regentprotocol.org/gw/{tool}/{path}` with `Authorization: Bearer <credential>`.
   https://docs.regentprotocol.org/gateway/tools-mcp.md

The full agent skill, with code and the meaning of every answer code:
https://docs.regentprotocol.org/skill.md

A marketplace where every purchase already runs through Regent: https://get4agent.com/AGENTS.md
