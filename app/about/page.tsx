"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import Image from "next/image";
import { ExternalLink, Target, Eye, Lightbulb } from "lucide-react";

export default function AboutPage() {
  return (
    <>
      <Navbar />
      <main className="flex-1">
        {/* Vision */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <Eye className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h1 className="mt-6 text-3xl font-bold text-white sm:text-4xl lg:text-5xl">
                Our Vision
              </h1>
              <blockquote className="mt-8 border-l-4 border-[#00C9B7] pl-6 text-left text-lg italic text-white/70 sm:text-xl">
                &quot;By 2030, every autonomous financial agent will have a verifiable identity, an immutable audit trail, and real-time behavioral compliance. Regent Protocol is building the infrastructure layer that makes this possible - starting on Solana.&quot;
              </blockquote>
            </motion.div>
          </div>
        </section>

        {/* Mission */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <Target className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h2 className="mt-6 text-3xl font-bold text-white sm:text-4xl">
                Our Mission
              </h2>
              <p className="mt-6 text-lg text-white/60">
                Regent Protocol exists because autonomous AI agents in finance need the same level of trust and accountability as human traders. We provide the compliance infrastructure - identity, audit, and real-time monitoring - that makes regulated finance with AI agents possible.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Why KYA */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <Lightbulb className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h2 className="mt-6 text-3xl font-bold text-white sm:text-4xl">
                Why KYA Matters
              </h2>
              <p className="mt-6 text-lg text-white/60">
                Know Your Agent (KYA) is the next evolution of compliance. Just as KYC verifies human identity, KYA verifies agent identity, behavior, and accountability. Without KYA, regulators cannot allow autonomous agents to manage real money.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Team */}
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
                The Team
              </h2>
              <p className="mt-4 text-lg text-white/60">
                Builders, operators, and strategists united by a mission
              </p>
            </motion.div>

            <div className="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {[
                {
                  name: "Sayat Kakzhanov",
                  role: "Founder & CEO",
                  bio: "TradFi + Web3 background. Ex-Compliance with National Bank connections. Driving the vision for regulated AI agent infrastructure.",
                  image: "/Sayat.png",
                  linkedin: "https://linkedin.com",
                },
                {
                  name: "Abay Aubakirov",
                  role: "Co-founder & CTO",
                  bio: "Full-stack engineer, Solana ecosystem builder. Smart contracts, React/Next.js, and infrastructure architecture.",
                  image: "/Abay.png",
                  linkedin: "https://linkedin.com",
                },
                {
                  name: "Marco Comuzzi",
                  role: "Advisor",
                  bio: "Strategic advisor with deep ecosystem connections. Guiding product strategy and market positioning.",
                  image: "/Marco3.png",
                  linkedin: "https://linkedin.com",
                },
              ].map((member, i) => (
                <motion.div
                  key={member.name}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.15 }}
                  className="rounded-xl border border-white/10 bg-[#0D1117] p-6 text-center"
                >
                  <div className="relative mx-auto h-32 w-32 overflow-hidden rounded-full border-2 border-[#00C9B7]/30">
                    <Image src={member.image} alt={member.name} fill className="object-cover" />
                  </div>
                  <h3 className="mt-6 text-lg font-semibold text-white">
                    {member.name}
                  </h3>
                  <p className="text-sm text-[#00C9B7]">{member.role}</p>
                  <p className="mt-3 text-sm text-white/60">{member.bio}</p>
                  <a
                    href={member.linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-4 inline-flex items-center gap-1.5 text-sm text-white/50 hover:text-[#00C9B7] transition-colors"
                  >
                    <ExternalLink size={16} />
                    LinkedIn
                  </a>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* Events */}
        <section id="events" className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center"
            >
              <h2 className="text-3xl font-bold text-white sm:text-4xl">
                Upcoming Events
              </h2>
              <div className="mt-10 rounded-xl border border-white/10 bg-[#0D1117] p-8">
                <p className="text-sm font-medium text-[#00C9B7]">Solana Summit Kazakhstan</p>
                <p className="mt-2 text-2xl font-bold text-white">May 22, 2026 - Almaty</p>
                <p className="mt-2 text-white/60">Meet the Regent Protocol team and learn about KYA infrastructure.</p>
              </div>
            </motion.div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
