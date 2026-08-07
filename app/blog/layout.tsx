import type { Metadata } from "next";

const TITLE = "Blog";
const DESCRIPTION =
  "Articles on AI agents, agent compliance, Know Your Agent (KYA), spend mandates, and building trust infrastructure for autonomous finance.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/blog" },
  openGraph: {
    url: "https://regentprotocol.org/blog",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

export default function BlogLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
