"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import Link from "next/link";
import {
  Layers,
  Database,
  Shield,
  Code,
  ArrowRight,
  GitBranch,
  FlaskConical,
  ExternalLink,
} from "lucide-react";
import SolanaLogo from "../components/SolanaLogo";

const architectureLayers = [
  {
    icon: Layers,
    title: "Solana Layer",
    description: "AgentRegistry, AuditAnchor, KYCDID programs on Solana mainnet.",
    bgClass: "bg-purple-500/10",
    textClass: "text-purple-400",
  },
  {
    icon: Database,
    title: "Celestia DA",
    description: "Blob storage for audit logs at $0.07/MB. True immutability with no freeze mechanism.",
    bgClass: "bg-violet-500/10",
    textClass: "text-violet-400",
  },
  {
    icon: Shield,
    title: "Guardian AI",
    description: "Python ML API with ONNX runtime. Behavioral scoring and real-time rule engine.",
    bgClass: "bg-[#00C9B7]/10",
    textClass: "text-[#00C9B7]",
  },
  {
    icon: Code,
    title: "Platform Layer",
    description: "Next.js dashboard, KYC flow, API key management, and analytics.",
    bgClass: "bg-white/10",
    textClass: "text-white",
  },
  {
    icon: GitBranch,
    title: "SDK Layer",
    description: "TypeScript, Python, and Rust (Anchor) clients for easy integration.",
    bgClass: "bg-orange-500/10",
    textClass: "text-orange-400",
  },
];

const comparisonData = [
  { metric: "Transaction Cost", solana: "$0.00025", l2: "$0.015", winner: "Solana", note: "60x cheaper" },
  { metric: "Throughput", solana: "1,300 TPS", l2: "0.04 TPS", winner: "Solana", note: "32,500x" },
  { metric: "Finality", solana: "150ms", l2: "7 min", winner: "Solana", note: "2,800x" },
  { metric: "DeFi TVL", solana: "$5.49B", l2: "Varies", winner: "Solana", note: "Ecosystem" },
];

const roadmap = [
  { quarter: "Q2 2026", title: "Testnet Launch", description: "SDK alpha, initial agent registry, Solana Summit KZ" },
  { quarter: "Q3 2026", title: "Mainnet MVP", description: "500 agents, Guardian AI v1, production audit chain" },
  { quarter: "Q4 2026", title: "Neon EVM", description: "Evaluation, 1,000 agents, cross-chain pilots" },
  { quarter: "Q1 2027", title: "Multi-chain", description: "Multi-chain support, 2,000 agents, institutional pilots" },
  { quarter: "Q2 2027", title: "Full Native", description: "Full Solana native, 5,000+ agents, enterprise tier" },
];

const sdks = [
  { name: "TypeScript / JavaScript", install: "npm install @regentprotocol/sdk", link: "https://github.com/abay94/regent-platform" },
  { name: "Python", install: "pip install regent-sdk", link: "https://github.com/abay94/regent-platform" },
  { name: "Rust (Anchor)", install: "cargo add regent-sdk", link: "https://github.com/abay94/regent-platform" },
];



export default function TechnologyPage() {
  return (
    <>
      <Navbar />
      <main className="flex-1">
        {/* Hero */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              <h1 className="text-3xl font-bold text-white sm:text-4xl lg:text-5xl">
                Technology
              </h1>
              <p className="mt-4 text-lg text-white/60">
                The architecture, stack, and roadmap behind Regent Protocol.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Architecture */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <h2 className="text-3xl font-bold text-white sm:text-4xl">
                Architecture Overview
              </h2>
              <p className="mt-4 text-lg text-white/60">
                Solana (settlement) → Celestia DA (audit storage) → Guardian AI (monitoring)
              </p>
            </motion.div>

            <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {architectureLayers.map((layer, i) => (
                <motion.div
                  key={layer.title}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.1 }}
                  className="rounded-xl border border-white/10 bg-[#0D1117] p-6"
                >
                  <div className={`flex h-10 w-10 items-center justify-center rounded-lg ${layer.bgClass}`}>
                    <layer.icon className={`h-5 w-5 ${layer.textClass}`} />
                  </div>
                  <h3 className="mt-4 text-lg font-semibold text-white">
                    {layer.title}
                  </h3>
                  <p className="mt-2 text-sm text-white/60">{layer.description}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Why Solana */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <h2 className="text-3xl font-bold text-white sm:text-4xl inline-flex items-center justify-center gap-3 flex-wrap">
                Why <SolanaLogo className="h-7 w-auto" /> Solana
              </h2>
              <p className="mt-4 text-lg text-white/60">
                The only chain with the speed, cost, and maturity for real-time agent compliance.
              </p>
            </motion.div>

            <div className="mt-16 overflow-hidden rounded-xl border border-white/10">
              <table className="w-full text-left">
                <thead className="bg-[#0D1117]">
                  <tr>
                    <th className="px-6 py-4 text-sm font-semibold text-white">Metric</th>
                    <th className="px-6 py-4 text-sm font-semibold text-[#9945FF]">Solana</th>
                    <th className="px-6 py-4 text-sm font-semibold text-white/60">Ethereum L2</th>
                    <th className="px-6 py-4 text-sm font-semibold text-white">Winner</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-white/10">
                  {comparisonData.map((row) => (
                    <tr key={row.metric} className="bg-[#0A1F3D]/50">
                      <td className="px-6 py-4 text-sm text-white">{row.metric}</td>
                      <td className="px-6 py-4 text-sm font-medium text-[#9945FF]">{row.solana}</td>
                      <td className="px-6 py-4 text-sm text-white/60">{row.l2}</td>
                      <td className="px-6 py-4 text-sm font-medium text-[#00C9B7]">{row.winner} ({row.note})</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </section>

        {/* Why Celestia */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <Database className="mx-auto h-10 w-10 text-[#7B2CBF]" />
              <h2 className="mt-6 text-3xl font-bold text-white sm:text-4xl">
                Why Celestia
              </h2>
              <p className="mt-6 text-lg text-white/60">
                Celestia provides dedicated Data Availability at $0.07/MB with true immutability - no freeze mechanism, full decentralization, and cryptographic guarantees that audit logs can never be altered or removed.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Security */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <Shield className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h2 className="mt-6 text-3xl font-bold text-white sm:text-4xl">
                Security Model
              </h2>
              <div className="mt-8 grid gap-4 text-left sm:grid-cols-2">
                {[
                  "Smart contract audit by leading security firm (in progress)",
                  "Multi-sig for all program upgrades",
                  "Rate limiting on every API endpoint",
                  "GDPR compliance framework (in progress)",
                  "Immutable audit trail on Celestia DA",
                  "Real-time anomaly detection via Guardian AI",
                ].map((item) => (
                  <div key={item} className="flex items-start gap-3 rounded-lg border border-white/10 bg-[#0D1117] p-4">
                    <Shield className="mt-0.5 h-4 w-4 shrink-0 text-[#00C9B7]" />
                    <span className="text-sm text-white/70">{item}</span>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        {/* Roadmap */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <h2 className="text-3xl font-bold text-white sm:text-4xl">
                Roadmap
              </h2>
              <p className="mt-4 text-lg text-white/60">
                From testnet to 5,000+ agents over the next 12 months.
              </p>
            </motion.div>

            <div className="mt-16 relative">
              {/* Timeline line */}
              <div className="absolute left-4 top-0 bottom-0 w-0.5 bg-white/10 sm:left-1/2 sm:-translate-x-px" />

              <div className="space-y-12">
                {roadmap.map((item, i) => (
                  <motion.div
                    key={item.quarter}
                    initial={{ opacity: 0, x: i % 2 === 0 ? -20 : 20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: i * 0.1 }}
                    className={`relative flex items-start gap-6 sm:items-center ${i % 2 === 0 ? "sm:flex-row" : "sm:flex-row-reverse"}`}
                  >
                    <div className="hidden sm:block sm:w-1/2 sm:px-8" />
                    <div className="absolute left-4 h-3 w-3 rounded-full bg-[#00C9B7] sm:left-1/2 sm:-translate-x-1.5" />
                    <div className="ml-12 sm:ml-0 sm:w-1/2 sm:px-8">
                      <div className="rounded-xl border border-white/10 bg-[#0D1117] p-6">
                        <span className="text-sm font-medium text-[#00C9B7]">{item.quarter}</span>
                        <h3 className="mt-1 text-lg font-semibold text-white">{item.title}</h3>
                        <p className="mt-2 text-sm text-white/60">{item.description}</p>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* SDK */}
        <section id="sdk" className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <h2 className="text-3xl font-bold text-white sm:text-4xl">
                SDK References
              </h2>
              <p className="mt-4 text-lg text-white/60">
                Get started with our multi-language SDK in under a minute.
              </p>
            </motion.div>

            <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {sdks.map((sdk, i) => (
                <motion.div
                  key={sdk.name}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.1 }}
                  className="rounded-xl border border-white/10 bg-[#0D1117] p-6"
                >
                  <h3 className="text-lg font-semibold text-white">
                    {sdk.name}
                  </h3>
                  <code className="mt-4 block rounded-lg bg-black/50 p-3 font-mono text-sm text-[#00C9B7]">
                    {sdk.install}
                  </code>
                  <a
                    href={sdk.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-4 inline-flex items-center gap-1.5 text-sm text-[#00C9B7] hover:underline"
                  >
                    View on GitHub <ExternalLink size={14} />
                  </a>
                </motion.div>
              ))}
            </div>
          </div>
        </section>


        {/* Testnet */}
        <section id="testnet" className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <FlaskConical className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h2 className="mt-6 text-3xl font-bold text-white sm:text-4xl">
                Testnet
              </h2>
              <p className="mt-6 text-lg text-white/60">
                Our testnet is live for early developers. Request faucet SOL, deploy your first AgentID, and anchor audit logs to Celestia - all without mainnet risk.
              </p>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:justify-center">
                <Link
                  href="/pilot"
                  className="inline-flex items-center justify-center gap-2 rounded-md bg-[#00C9B7] px-6 py-3 text-sm font-semibold text-black hover:bg-[#00b8a8] transition-colors"
                >
                  Apply for Testnet Access <ArrowRight size={16} />
                </Link>
                <a
                  href="https://github.com/abay94/regent-platform"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-2 rounded-md border border-white/20 px-6 py-3 text-sm font-semibold text-white hover:bg-white/5 transition-colors"
                >
                  Read Testnet Docs <ExternalLink size={16} />
                </a>
              </div>
            </motion.div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
