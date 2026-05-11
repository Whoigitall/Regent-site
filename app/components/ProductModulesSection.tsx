"use client";

import { motion } from "framer-motion";
import { Fingerprint, Link2, Shield } from "lucide-react";

const products = [
  {
    icon: Fingerprint,
    title: "AgentID",
    description: "On-chain agent identity via Solana Agent Registry with Metaplex Core. DID:SOL decentralized identifiers and on-chain KYC verification.",
    features: ["Metaplex Core Registry", "DID:SOL Identifiers", "On-chain KYC"],
  },
  {
    icon: Link2,
    title: "Audit Chain",
    description: "Immutable audit storage on Celestia DA with Solana ledger anchors. Merkle root anchoring for efficient batch proofs.",
    features: ["Celestia DA Storage", "Solana Anchors", "Merkle Proofs"],
  },
  {
    icon: Shield,
    title: "Guardian AI",
    description: "Real-time behavioral monitoring with rule-based and ML scoring via ONNX. Automatic stop on risk threshold breach.",
    features: ["Real-time Monitoring", "ML Scoring (ONNX)", "Auto-stop"],
  },
];

export default function ProductModulesSection() {
  return (
    <section className="w-full bg-black py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-center"
        >
          <h2 className="text-3xl font-bold text-white sm:text-4xl">
            Product Stack
          </h2>
          <p className="mt-3 text-lg text-white/50">
            Identity, audit, and monitoring. Three integrated modules.
          </p>
        </motion.div>

        <div className="mt-14 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {products.map((product, i) => (
            <motion.div
              key={product.title}
              initial={{ opacity: 0, y: 12 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.4, delay: i * 0.1 }}
              className="rounded-lg border border-white/10 bg-[#0D1117] p-6"
            >
              <div className="flex h-10 w-10 items-center justify-center rounded-md bg-[#00C9B7]/10">
                <product.icon className="h-5 w-5 text-[#00C9B7]" />
              </div>
              <h3 className="mt-5 text-lg font-semibold text-white">
                {product.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-white/50">
                {product.description}
              </p>
              <ul className="mt-5 space-y-1.5">
                {product.features.map((feature) => (
                  <li key={feature} className="flex items-center gap-2 text-sm text-white/60">
                    <span className="h-1 w-1 rounded-full bg-[#00C9B7]" />
                    {feature}
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
