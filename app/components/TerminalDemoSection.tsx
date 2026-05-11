"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowRight, Copy, Check } from "lucide-react";
import { useState } from "react";

export default function TerminalDemoSection() {
  const [copied, setCopied] = useState(false);

  const copyCode = () => {
    navigator.clipboard.writeText("npm install @regentprotocol/sdk");
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

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
            Start in 60 Seconds
          </h2>
          <p className="mt-4 text-lg text-white/60">
            Get up and running with the Regent SDK in under a minute.
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="mx-auto mt-12 max-w-2xl"
        >
          <div className="overflow-hidden rounded-xl border border-white/10 bg-[#0D1117] shadow-2xl">
            <div className="flex items-center gap-2 border-b border-white/10 bg-[#161B22] px-4 py-3">
              <div className="h-3 w-3 rounded-full bg-red-500" />
              <div className="h-3 w-3 rounded-full bg-yellow-500" />
              <div className="h-3 w-3 rounded-full bg-green-500" />
              <span className="ml-2 text-xs text-white/40">bash - regent-sdk</span>
            </div>
            <div className="p-6">
              <div className="flex items-start justify-between gap-4">
                <code className="font-mono text-sm text-[#00C9B7]">
                  <span className="text-white/40">$</span> npm install @regentprotocol/sdk
                </code>
                <button
                  onClick={copyCode}
                  className="shrink-0 rounded-md p-1.5 text-white/40 hover:bg-white/10 hover:text-white transition-colors"
                >
                  {copied ? <Check size={16} /> : <Copy size={16} />}
                </button>
              </div>
              <code className="mt-3 block font-mono text-sm text-[#00C9B7]">
                <span className="text-white/40"># or</span>
              </code>
              <code className="mt-1 block font-mono text-sm text-[#00C9B7]">
                <span className="text-white/40">$</span> pip install regent-sdk
              </code>
            </div>
          </div>

          <div className="mt-8 text-center">
            <Link
              href="/technology"
              className="inline-flex items-center gap-2 rounded-md bg-[#00C9B7] px-6 py-3 text-sm font-semibold text-black hover:bg-[#00b8a8] transition-colors"
            >
              View Documentation
              <ArrowRight size={16} />
            </Link>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
