import type { Metadata } from "next";
import { faqs } from "./faqs";

const TITLE = "Pilot Program";
const DESCRIPTION =
  "Run a zero-risk pilot of Regent's agent firewall: start in observe mode, see exactly what would be blocked, then switch to enforcement — no code changes to your agents.";

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/pilot" },
  openGraph: {
    url: "https://regentprotocol.org/pilot",
    title: `${TITLE} — Regent Protocol`,
    description: DESCRIPTION,
  },
};

// FAQPage schema generated from the SAME faqs used on the visible page — so the
// structured data always mirrors what a user sees (required for FAQ rich results).
const faqLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map((f) => ({
    "@type": "Question",
    name: f.question,
    acceptedAnswer: { "@type": "Answer", text: f.answer },
  })),
};

export default function PilotLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqLd) }}
      />
      {children}
    </>
  );
}
