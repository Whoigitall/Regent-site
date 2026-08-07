import type { Metadata } from "next";

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

export default function PilotLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
}
