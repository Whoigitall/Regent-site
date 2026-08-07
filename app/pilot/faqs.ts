// Single source of truth for the Pilot FAQ — rendered visibly by page.tsx AND
// used to generate FAQPage structured data in layout.tsx, so the schema can
// never drift from the visible content (required for valid FAQ rich results).
export const faqs = [
  {
    question: "Who qualifies for the Pilot Program?",
    answer:
      "Solana-based DeFi protocols, fintechs with compliance requirements, and AI agent frameworks. Minimum: 1 active agent or 100+ daily transactions.",
  },
  {
    question: "How long is the pilot engagement?",
    answer:
      "The pilot is a structured 14-day engagement where we work with your team to integrate KYA infrastructure into your product.",
  },
  {
    question: "What do I get during the pilot?",
    answer:
      "KYA infrastructure integration, custom AgentID setup, audit chain configuration, Guardian AI monitoring rules, and a dedicated support channel.",
  },
  {
    question: "Is there a free trial?",
    answer:
      "The Starter tier is effectively a 14-day structured pilot. We work alongside your team during this period at no additional setup cost.",
  },
  {
    question: "Can I switch tiers later?",
    answer:
      "Yes, you can upgrade or downgrade at any time. Upgrades are prorated, and downgrades take effect at the next billing cycle.",
  },
  {
    question: "Do you offer custom enterprise pricing?",
    answer:
      "Absolutely. Contact us at info@regentprotocol.org for custom SLAs, on-premise deployment, and white-label options.",
  },
];
