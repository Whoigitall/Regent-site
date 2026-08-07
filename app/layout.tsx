import type { Metadata } from "next";
import { Inter, Orbitron, Rajdhani } from "next/font/google";
import "./globals.css";
import PostHogInit from "./posthog-init";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const orbitron = Orbitron({
  variable: "--font-orbitron",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800", "900"],
});

const rajdhani = Rajdhani({
  variable: "--font-rajdhani",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://regentprotocol.org"),
  title: {
    default:
      "Regent Protocol — Verifiable Agent Infrastructure for Regulated Finance",
    template: "%s — Regent Protocol",
  },
  description:
    "KYA (Know Your Agent): identity, spend mandates, real-time compliance, and immutable audit for autonomous AI agents. Built on Solana, anchored to Celestia.",
  keywords: [
    "AI agents",
    "agent compliance",
    "Know Your Agent",
    "KYA",
    "KYC",
    "spend mandates",
    "agent firewall",
    "Solana",
    "Celestia",
    "Regent Protocol",
  ],
  applicationName: "Regent Protocol",
  alternates: { canonical: "/" },
  // Favicon is provided by the app/icon.png file convention (auto-injected).
  robots: { index: true, follow: true },
  openGraph: {
    type: "website",
    siteName: "Regent Protocol",
    url: "https://regentprotocol.org",
    title:
      "Regent Protocol — Verifiable Agent Infrastructure for Regulated Finance",
    description:
      "KYA (Know Your Agent): identity, spend mandates, real-time compliance, and immutable audit for autonomous AI agents. Built on Solana.",
    locale: "en_US",
    images: [{ url: "/logo-full.png", alt: "Regent Protocol" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Regent Protocol — Verifiable Agent Infrastructure",
    description:
      "KYA (Know Your Agent): identity, spend mandates, and audit for autonomous AI agents on Solana.",
    images: ["/logo-full.png"],
  },
};

// Structured data (schema.org) — only verified facts. Lets AI engines and Google
// recognize Regent as an entity, its founders, and its press/partner context.
const organizationLd = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "Regent Protocol",
  alternateName: "Regent",
  url: "https://regentprotocol.org",
  logo: "https://regentprotocol.org/logo-full.png",
  description:
    "Compliance and identity infrastructure for the agentic economy: Know Your Agent (KYA) verification, on-chain spending mandates, a risk engine, and immutable audit for autonomous AI agents. Built on Solana.",
  founder: [
    {
      "@type": "Person",
      name: "Sayat Kakzhanov",
      jobTitle: "Founder & CEO",
      sameAs: "https://www.linkedin.com/in/kakzhanov/",
    },
    {
      "@type": "Person",
      name: "Abay Aubakirov",
      jobTitle: "Co-founder & CTO",
      sameAs: "https://www.linkedin.com/in/abay-aubakirov-74a90362/",
    },
  ],
  address: { "@type": "PostalAddress", addressCountry: "KZ" },
  sameAs: [
    "https://www.linkedin.com/company/regentprotocol/",
    "https://x.com/whoigital",
  ],
  knowsAbout: [
    "Know Your Agent",
    "AI agent compliance",
    "spending mandates",
    "AML",
    "Solana",
    "autonomous payments",
  ],
  subjectOf: {
    "@type": "NewsArticle",
    headline:
      "Как два казахстанских стартапа доверили деньги ИИ, не дав потратить лишнего",
    url: "https://forbes.kz/articles/kak-dva-kazahstanskih-startapa-doverili-dengi-ii-ne-dav-potratit-lishnego-557af7",
    datePublished: "2026-07-23",
    publisher: { "@type": "Organization", name: "Forbes Kazakhstan" },
  },
};

const websiteLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "Regent Protocol",
  url: "https://regentprotocol.org",
  publisher: {
    "@type": "Organization",
    name: "Regent Protocol",
    url: "https://regentprotocol.org",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${orbitron.variable} ${rajdhani.variable} dark h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-black text-white font-sans">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(organizationLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteLd) }}
        />
        <PostHogInit />
        {children}
      </body>
    </html>
  );
}
