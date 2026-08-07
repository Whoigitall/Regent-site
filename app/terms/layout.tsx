import type { Metadata } from "next";

const TITLE = "Terms of Service";
const DESCRIPTION =
  "The terms governing use of Regent Protocol's website and services.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/terms" },
  openGraph: {
    url: "https://regentprotocol.org/terms",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

export default function TermsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
