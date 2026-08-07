// Homepage FAQ — single source of truth for both the visible section and the
// FAQPage structured data (they must match for valid rich results / AEO).
export const homeFaqs = [
  {
    question: "What is Know Your Agent (KYA)?",
    answer:
      "Know Your Agent (KYA) is a compliance protocol that verifies AI agents before they execute financial transactions. It ensures that every autonomous payment has a verified sender, approved limits, and an immutable audit trail.",
  },
  {
    question: "How does Regent Protocol prevent unauthorized AI spending?",
    answer:
      "Regent Protocol uses spending mandates — programmable rules that define what an AI agent can spend, on what, and up to what limit. A transaction outside those rules is denied before it executes, and the agent never holds the payment credentials itself.",
  },
  {
    question: "What is an AgentID?",
    answer:
      "AgentID is a unique decentralized identifier (DID) assigned to every AI agent in the Regent network. It links the agent to its KYA verification, mandates, and audit history.",
  },
];
