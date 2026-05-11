"use client";

import { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { Menu, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

const navLinks = [
  { href: "/", label: "Home" },
  { href: "/about", label: "About" },
  { href: "/technology", label: "Technology" },
  { href: "/pilot", label: "Pilot" },
  { href: "/blog", label: "Blog" },
];

export default function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-white/10 bg-black/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
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

        <nav className="hidden md:flex items-center gap-8">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="text-sm font-medium text-white/70 hover:text-[#00C9B7] transition-colors"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="hidden md:flex items-center gap-2">
          <a
            href="https://detect.regentprotocol.org/dashboard"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-md border border-white/20 px-3 py-2 text-sm font-medium text-white/70 hover:text-white hover:border-white/40 transition-colors"
          >
            Agent Detector
          </a>
          <a
            href="https://web.regentprotocol.org/dashboard"
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-md bg-[#00C9B7] px-3 py-2 text-sm font-medium text-black hover:bg-[#00b8a8] transition-colors"
          >
            Live Platform
          </a>
        </div>

        <button
          onClick={() => setMobileOpen(!mobileOpen)}
          className="md:hidden p-2 text-white"
        >
          {mobileOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden border-t border-white/10 bg-black"
          >
            <div className="flex flex-col gap-4 px-4 py-6">
              {navLinks.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  onClick={() => setMobileOpen(false)}
                  className="text-base font-medium text-white/70 hover:text-[#00C9B7] transition-colors"
                >
                  {link.label}
                </Link>
              ))}
              <a
                href="https://detect.regentprotocol.org/dashboard"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-md border border-white/20 px-4 py-2 text-sm font-medium text-white/70 text-center hover:text-white transition-colors"
              >
                Agent Detector
              </a>
              <a
                href="https://web.regentprotocol.org/dashboard"
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-md bg-[#00C9B7] px-4 py-2 text-sm font-medium text-black text-center hover:bg-[#00b8a8] transition-colors"
              >
                Live Platform
              </a>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
