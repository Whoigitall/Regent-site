"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { TrendingUp, Zap, Clock, DollarSign, ArrowRight } from "lucide-react";

const metrics = [
  {
    icon: DollarSign,
    title: "60x Cheaper",
    value: "$0.00025",
    description: "vs $0.015 per transaction on Ethereum L2",
  },
  {
    icon: TrendingUp,
    title: "32,500x Throughput",
    value: "1,300 TPS",
    description: "vs 0.04 TPS on traditional settlement",
  },
  {
    icon: Clock,
    title: "150ms Finality",
    value: "Post-Alpenglow",
    description: "Sub-second confirmation time",
  },
  {
    icon: Zap,
    title: "$5.49B Ecosystem",
    value: "DeFi TVL",
    description: "Backing infrastructure maturity",
  },
];

export default function WhySolanaSection() {
  return (
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
            Why We Chose Solana
          </h2>
          <p className="mt-4 text-lg text-white/60">
            78% cost reduction. 145% Year 1 ROI. Sub-second finality.
          </p>
        </motion.div>

        <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {metrics.map((metric, i) => (
            <motion.div
              key={metric.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="rounded-xl border border-white/10 bg-black/40 p-6 backdrop-blur-sm"
            >
              <metric.icon className="h-8 w-8 text-[#00C9B7]" />
              <h3 className="mt-4 text-xl font-semibold text-white">
                {metric.title}
              </h3>
              <p className="mt-2 text-2xl font-bold text-[#00C9B7]">{metric.value}</p>
              <p className="mt-1 text-sm text-white/50">{metric.description}</p>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="mt-10 text-center"
        >
          <Link
            href="/technology"
            className="inline-flex items-center gap-2 text-sm font-medium text-[#00C9B7] hover:underline"
          >
            Read our architecture analysis
            <ArrowRight size={16} />
          </Link>
        </motion.div>
      </div>
    </section>
  );
}
