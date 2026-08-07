import type { Metadata } from "next";

const TITLE = "About";
const DESCRIPTION =
  "Regent Protocol builds compliance and identity infrastructure for the agentic economy — Know Your Agent (KYA) verification, spend controls, and immutable audit for autonomous AI agents.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/about" },
  openGraph: {
    url: "https://regentprotocol.org/about",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

export default function AboutLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
