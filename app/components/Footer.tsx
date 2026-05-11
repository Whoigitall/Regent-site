"use client";

import Link from "next/link";
import Image from "next/image";
import { GitBranch, Globe, Mail, ExternalLink } from "lucide-react";

const footerColumns = [
  {
    title: "Developers",
    links: [
      { label: "Documentation", href: "/technology" },
      { label: "SDK Reference", href: "/technology#sdk" },
      { label: "GitHub", href: "https://github.com/Whoigitall", external: true },
      { label: "Testnet", href: "/technology#testnet" },
    ],
  },
  {
    title: "Enterprise",
    links: [
      { label: "Solutions", href: "/technology" },
      { label: "Pilot Program", href: "/pilot" },
      { label: "Contact", href: "mailto:hello@regentprotocol.org", external: true },
    ],
  },
  {
    title: "Community",
    links: [
      { label: "Blog", href: "/blog" },
      { label: "Events", href: "/about#events" },
      { label: "LinkedIn", href: "https://linkedin.com", external: true },
      { label: "X (Twitter)", href: "https://x.com/whoigital", external: true },
      { label: "Discord", href: "https://discord.gg", external: true },
    ],
  },
  {
    title: "Products",
    links: [
      { label: "Live Platform", href: "https://web.regentprotocol.org/dashboard", external: true },
      { label: "Agent Detector", href: "https://detect.regentprotocol.org/dashboard", external: true },
    ],
  },
  {
    title: "Legal",
    links: [
      { label: "Terms of Use", href: "/terms" },
      { label: "Privacy Policy", href: "/privacy" },
    ],
  },
];

export default function Footer() {
  return (
    <footer className="w-full border-t border-white/10 bg-[#0A1F3D]">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-3 lg:grid-cols-6">
          <div className="col-span-2 md:col-span-3 lg:col-span-1">
            <Link href="/" className="flex items-center gap-2">
              <Image
                src="/R white-Photoroom.png"
                alt="Regent Protocol"
                width={32}
                height={32}
                className="h-8 w-auto"
              />
              <span className="font-[family-name:var(--font-orbitron)] text-lg font-bold tracking-wide text-white">
                REGENT
              </span>
            </Link>
            <p className="mt-4 text-sm text-white/60">
              Verifiable Agent Infrastructure for Regulated Finance on Solana.
            </p>
            <div className="mt-4 flex flex-wrap gap-3">
              <a href="https://github.com/Whoigitall" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-white/60 hover:text-[#00C9B7] transition-colors">
                <GitBranch size={16} />
                GitHub
              </a>
              <a href="https://x.com/whoigital" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-white/60 hover:text-[#00C9B7] transition-colors">
                <Globe size={16} />
                X
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1.5 text-sm text-white/60 hover:text-[#00C9B7] transition-colors">
                <ExternalLink size={16} />
                LinkedIn
              </a>
              <a href="mailto:hello@regentprotocol.org" className="inline-flex items-center gap-1.5 text-sm text-white/60 hover:text-[#00C9B7] transition-colors">
                <Mail size={16} />
                Email
              </a>
            </div>
          </div>

          {footerColumns.map((column) => (
            <div key={column.title}>
              <h3 className="text-sm font-semibold text-white">{column.title}</h3>
              <ul className="mt-4 space-y-2">
                {column.links.map((link) => (
                  <li key={link.label}>
                    {link.external ? (
                      <a
                        href={link.href}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-sm text-white/60 hover:text-[#00C9B7] transition-colors"
                      >
                        {link.label}
                      </a>
                    ) : (
                      <Link
                        href={link.href}
                        className="text-sm text-white/60 hover:text-[#00C9B7] transition-colors"
                      >
                        {link.label}
                      </Link>
                    )}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-12 border-t border-white/10 pt-8 text-center">
          <p className="text-sm text-white/40">
            © {new Date().getFullYear()} Regent Protocol. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
