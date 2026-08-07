import type { Metadata } from "next";

const TITLE = "Technology";
const DESCRIPTION =
  "How Regent enforces policy on AI agents: Know Your Agent (KYA) identity, spend mandates, the Guardian risk engine, vaulted credentials, and Solana-anchored audit trails.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/technology" },
  openGraph: {
    url: "https://regentprotocol.org/technology",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

export default function TechnologyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
