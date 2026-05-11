"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, ExternalLink } from "lucide-react";
import SolanaLogo from "./SolanaLogo";

export default function HeroSection() {
  return (
    <section className="relative w-full bg-black py-24 sm:py-32 lg:py-40">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col items-center text-center">
          <motion.div
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-[#0A1F3D] px-4 py-1.5 text-sm text-[#00C9B7]"
          >
            <span className="inline-flex items-center gap-1.5">Built on <SolanaLogo className="h-3.5 w-auto inline" /> Solana</span>
            <span className="text-white/20">/</span>
            <span>AIFC Sandbox</span>
            <span className="text-white/20">/</span>
            <span>Summit Almaty 2026</span>
          </motion.div>

          <motion.h1
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.1 }}
            className="mt-8 max-w-4xl text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl"
          >
            Verifiable Agent Infrastructure{" "}
            <span className="text-[#00C9B7]">for Regulated Finance</span>
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="mt-6 max-w-2xl text-lg text-white/50"
          >
            KYA (Know Your Agent): identity, audit, and real-time compliance for autonomous AI agents. Built on <span className="inline-flex items-center gap-1"><SolanaLogo className="h-4 w-auto inline" /> Solana</span>. Anchored to Celestia.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.3 }}
            className="mt-10 flex flex-col gap-3 sm:flex-row"
          >
            <a
              href="https://docs.regentprotocol.org/"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 rounded-md border border-white/20 px-5 py-2.5 text-sm font-medium text-white hover:border-white/40 transition-colors"
            >
              Explore Documentation
              <ArrowRight size={14} />
            </a>
            <Link
              href="/pilot"
              className="inline-flex items-center justify-center gap-2 rounded-md bg-[#00C9B7] px-5 py-2.5 text-sm font-medium text-black hover:bg-[#00b8a8] transition-colors"
            >
              Apply for Pilot
            </Link>
            <a
              href="https://web.regentprotocol.org/dashboard"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 rounded-md border border-[#00C9B7]/30 px-5 py-2.5 text-sm font-medium text-[#00C9B7] hover:bg-[#00C9B7]/10 transition-colors"
            >
              Live Platform
              <ExternalLink size={14} />
            </a>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
