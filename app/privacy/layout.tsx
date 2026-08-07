import type { Metadata } from "next";

const TITLE = "Privacy Policy";
const DESCRIPTION =
  "How Regent Protocol collects, uses, and protects data across its website and services.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/privacy" },
  openGraph: {
    url: "https://regentprotocol.org/privacy",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

export default function PrivacyLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
