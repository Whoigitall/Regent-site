"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import { BookOpen, ArrowRight, Mail } from "lucide-react";
import { useState } from "react";

export default function BlogPage() {
  const [email, setEmail] = useState("");
  const [subscribed, setSubscribed] = useState(false);

  const handleSubscribe = (e: React.FormEvent) => {
    e.preventDefault();
    setSubscribed(true);
  };

  return (
    <>
      <Navbar />
      <main className="flex-1">
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              <BookOpen className="mx-auto h-12 w-12 text-[#00C9B7]" />
              <h1 className="mt-6 text-3xl font-bold text-white sm:text-4xl lg:text-5xl">
                Blog
              </h1>
              <p className="mt-4 text-lg text-white/60">
                Coming Soon
              </p>
              <p className="mt-4 max-w-2xl mx-auto text-white/50">
                We&apos;re preparing in-depth articles on Solana agent compliance, KYA architecture, and ecosystem updates. Subscribe to be notified.
              </p>

              {subscribed ? (
                <div className="mt-8 inline-flex items-center gap-2 rounded-lg border border-[#00C9B7]/30 bg-[#0D1117] px-6 py-3 text-[#00C9B7]">
                  <Mail size={18} />
                  You&apos;re on the list - we&apos;ll notify you when we publish.
                </div>
              ) : (
                <form
                  onSubmit={handleSubscribe}
                  className="mt-8 mx-auto flex max-w-md flex-col gap-3 sm:flex-row"
                >
                  <input
                    required
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="your@email.com"
                    className="flex-1 rounded-lg border border-white/10 bg-[#0D1117] px-4 py-3 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                  />
                  <button
                    type="submit"
                    className="inline-flex items-center justify-center gap-2 rounded-lg bg-[#00C9B7] px-6 py-3 text-sm font-semibold text-black hover:bg-[#00b8a8] transition-colors"
                  >
                    Subscribe
                    <ArrowRight size={16} />
                  </button>
                </form>
              )}
            </motion.div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
