"use client";

import { motion } from "framer-motion";
import { Calendar, ExternalLink, MessageCircle } from "lucide-react";

export default function EventsBanner() {
  return (
    <section className="w-full bg-[#0A1F3D] py-16 sm:py-20">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="flex flex-col items-center gap-6 text-center sm:flex-row sm:justify-between sm:text-left"
        >
          <div>
            <div className="flex items-center gap-2 text-[#00C9B7]">
              <Calendar size={20} />
              <span className="text-sm font-medium">Upcoming Event</span>
            </div>
            <h3 className="mt-3 text-2xl font-bold text-white sm:text-3xl">
              Meet us at Solana Summit Kazakhstan
            </h3>
            <p className="mt-2 text-white/60">
              May 22, 2026 - Almaty, Kazakhstan
            </p>
          </div>
          <div className="flex flex-col gap-3 sm:flex-row">
            <a
              href="https://solana.com/summit"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 rounded-md bg-[#00C9B7] px-6 py-3 text-sm font-semibold text-black hover:bg-[#00b8a8] transition-colors"
            >
              Register for Summit
              <ExternalLink size={16} />
            </a>
            <a
              href="mailto:info@regentprotocol.org"
              className="inline-flex items-center justify-center gap-2 rounded-md border border-white/20 px-6 py-3 text-sm font-semibold text-white hover:bg-white/5 transition-colors"
            >
              Schedule a Meeting
              <MessageCircle size={16} />
            </a>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
