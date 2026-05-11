import type { Metadata } from "next";
import { Inter, Orbitron, Rajdhani } from "next/font/google";
import "./globals.css";

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
  title: "Regent Protocol - Verifiable Agent Infrastructure for Regulated Finance",
  description: "KYA (Know Your Agent): identity, audit, and real-time compliance for autonomous AI agents. Built on Solana. Anchored to Celestia.",
  keywords: ["AI agents", "compliance", "Solana", "Celestia", "KYA", "KYC", "DeFi", "Regent Protocol"],
  icons: {
    icon: "/icon.png",
  },
  openGraph: {
    title: "Regent Protocol",
    description: "Verifiable Agent Infrastructure for Regulated Finance on Solana",
    type: "website",
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
        {children}
      </body>
    </html>
  );
}
