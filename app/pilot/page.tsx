"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import { useState } from "react";
import {
  Rocket,
  CheckCircle,
  ArrowRight,
  ChevronDown,
} from "lucide-react";

const tiers = [
  {
    name: "Starter",
    price: "$99/mo",
    agents: "Up to 5",
    support: "Email",
    features: [
      "KYA infrastructure integration",
      "Custom AgentID setup",
      "Audit chain configuration",
      "Community support",
    ],
  },
  {
    name: "Growth",
    price: "$299/mo",
    agents: "Up to 25",
    support: "Priority",
    features: [
      "Everything in Starter",
      "Guardian AI monitoring rules",
      "Priority API access",
      "Monthly compliance report",
    ],
  },
  {
    name: "Enterprise",
    price: "$499/mo",
    agents: "Unlimited",
    support: "Dedicated",
    features: [
      "Everything in Growth",
      "Dedicated support channel",
      "Custom SLA",
      "On-premise deployment option",
      "White-label dashboard",
    ],
  },
];

const faqs = [
  {
    question: "Who qualifies for the Pilot Program?",
    answer:
      "Solana-based DeFi protocols, fintechs with compliance requirements, and AI agent frameworks. Minimum: 1 active agent or 100+ daily transactions.",
  },
  {
    question: "How long is the pilot engagement?",
    answer:
      "The pilot is a structured 14-day engagement where we work with your team to integrate KYA infrastructure into your product.",
  },
  {
    question: "What do I get during the pilot?",
    answer:
      "KYA infrastructure integration, custom AgentID setup, audit chain configuration, Guardian AI monitoring rules, and a dedicated support channel.",
  },
  {
    question: "Is there a free trial?",
    answer:
      "The Starter tier is effectively a 14-day structured pilot. We work alongside your team during this period at no additional setup cost.",
  },
  {
    question: "Can I switch tiers later?",
    answer:
      "Yes, you can upgrade or downgrade at any time. Upgrades are prorated, and downgrades take effect at the next billing cycle.",
  },
  {
    question: "Do you offer custom enterprise pricing?",
    answer:
      "Absolutely. Contact us at info@regentprotocol.org for custom SLAs, on-premise deployment, and white-label options.",
  },
];

export default function PilotPage() {
  const [openFaq, setOpenFaq] = useState<number | null>(null);
  const [form, setForm] = useState({
    name: "",
    email: "",
    company: "",
    website: "",
    agents: "",
    useCase: "",
    message: "",
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

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
              <Rocket className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h1 className="mt-6 text-3xl font-bold text-white sm:text-4xl lg:text-5xl">
                Pilot Program
              </h1>
              <p className="mt-4 text-lg text-white/60">
                14-day structured engagement for early adopters. We work with your team to integrate KYA infrastructure into your Solana-based protocol or fintech product.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Who Qualifies */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-center text-3xl font-bold text-white sm:text-4xl">
                Who Qualifies
              </h2>
              <div className="mt-10 grid gap-4 sm:grid-cols-2">
                {[
                  "Solana-based DeFi protocols",
                  "Fintechs with compliance requirements",
                  "AI agent frameworks",
                  "Minimum 1 active agent or 100+ daily transactions",
                ].map((item) => (
                  <div
                    key={item}
                    className="flex items-center gap-3 rounded-lg border border-white/10 bg-[#0D1117] p-4"
                  >
                    <CheckCircle className="h-5 w-5 shrink-0 text-[#00C9B7]" />
                    <span className="text-sm text-white/80">{item}</span>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        {/* What You Get */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-center text-3xl font-bold text-white sm:text-4xl">
                What You Get
              </h2>
              <div className="mt-10 grid gap-4 sm:grid-cols-2">
                {[
                  "KYA infrastructure integration",
                  "Custom AgentID setup",
                  "Audit chain configuration",
                  "Guardian AI monitoring rules",
                  "Dedicated support channel",
                ].map((item) => (
                  <div
                    key={item}
                    className="flex items-center gap-3 rounded-lg border border-white/10 bg-[#0D1117] p-4"
                  >
                    <CheckCircle className="h-5 w-5 shrink-0 text-[#00C9B7]" />
                    <span className="text-sm text-white/80">{item}</span>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        {/* Pricing */}
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
                Pricing
              </h2>
              <p className="mt-4 text-lg text-white/60">
                Transparent pricing that scales with your agent fleet.
              </p>
            </motion.div>

            <div className="mt-16 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {tiers.map((tier, i) => (
                <motion.div
                  key={tier.name}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: i * 0.1 }}
                  className={`rounded-xl border p-6 ${
                    tier.name === "Growth"
                      ? "border-[#00C9B7]/30 bg-[#0D1117] ring-1 ring-[#00C9B7]/20"
                      : "border-white/10 bg-[#0D1117]"
                  }`}
                >
                  <h3 className="text-lg font-semibold text-white">
                    {tier.name}
                  </h3>
                  <p className="mt-2 text-3xl font-bold text-[#00C9B7]">
                    {tier.price}
                  </p>
                  <div className="mt-4 space-y-2 text-sm text-white/60">
                    <p>
                      <span className="text-white">Agents:</span> {tier.agents}
                    </p>
                    <p>
                      <span className="text-white">Support:</span> {tier.support}
                    </p>
                  </div>
                  <ul className="mt-6 space-y-2">
                    {tier.features.map((feature) => (
                      <li
                        key={feature}
                        className="flex items-start gap-2 text-sm text-white/70"
                      >
                        <CheckCircle className="mt-0.5 h-4 w-4 shrink-0 text-[#00C9B7]" />
                        {feature}
                      </li>
                    ))}
                  </ul>
                </motion.div>
              ))}
            </div>
          </div>
        </section>

        {/* FAQ */}
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-center text-3xl font-bold text-white sm:text-4xl">
                Frequently Asked Questions
              </h2>
              <div className="mt-10 space-y-3">
                {faqs.map((faq, i) => (
                  <div
                    key={i}
                    className="rounded-lg border border-white/10 bg-[#0D1117]"
                  >
                    <button
                      onClick={() =>
                        setOpenFaq(openFaq === i ? null : i)
                      }
                      className="flex w-full items-center justify-between px-5 py-4 text-left"
                    >
                      <span className="font-medium text-white">
                        {faq.question}
                      </span>
                      <ChevronDown
                        className={`h-5 w-5 text-white/50 transition-transform ${
                          openFaq === i ? "rotate-180" : ""
                        }`}
                      />
                    </button>
                    {openFaq === i && (
                      <div className="px-5 pb-4 text-sm text-white/60">
                        {faq.answer}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        {/* Apply Form */}
        <section className="w-full bg-[#0A1F3D] py-20 sm:py-28">
          <div className="mx-auto max-w-2xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-center text-3xl font-bold text-white sm:text-4xl">
                Apply for the Pilot
              </h2>
              <p className="mt-4 text-center text-lg text-white/60">
                Tell us about your project and we&#39;ll be in touch within 48 hours.
              </p>

              {submitted ? (
                <div className="mt-10 rounded-xl border border-[#00C9B7]/30 bg-[#0D1117] p-8 text-center">
                  <CheckCircle className="mx-auto h-12 w-12 text-[#00C9B7]" />
                  <h3 className="mt-4 text-xl font-semibold text-white">
                    Application Received
                  </h3>
                  <p className="mt-2 text-white/60">
                    We&#39;ll review your application and get back to you within 48 hours.
                  </p>
                </div>
              ) : (
                <form
                  onSubmit={handleSubmit}
                  className="mt-10 space-y-5"
                >
                  <div className="grid gap-5 sm:grid-cols-2">
                    <div>
                      <label className="block text-sm font-medium text-white/70">
                        Name
                      </label>
                      <input
                        required
                        type="text"
                        value={form.name}
                        onChange={(e) =>
                          setForm({ ...form, name: e.target.value })
                        }
                        className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                        placeholder="Your name"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-white/70">
                        Email
                      </label>
                      <input
                        required
                        type="email"
                        value={form.email}
                        onChange={(e) =>
                          setForm({ ...form, email: e.target.value })
                        }
                        className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                        placeholder="you@company.com"
                      />
                    </div>
                  </div>
                  <div className="grid gap-5 sm:grid-cols-2">
                    <div>
                      <label className="block text-sm font-medium text-white/70">
                        Company
                      </label>
                      <input
                        required
                        type="text"
                        value={form.company}
                        onChange={(e) =>
                          setForm({ ...form, company: e.target.value })
                        }
                        className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                        placeholder="Company name"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-white/70">
                        Website
                      </label>
                      <input
                        type="url"
                        value={form.website}
                        onChange={(e) =>
                          setForm({ ...form, website: e.target.value })
                        }
                        className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                        placeholder="https://..."
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-white/70">
                      Estimated Agent Count
                    </label>
                    <input
                      required
                      type="number"
                      value={form.agents}
                      onChange={(e) =>
                        setForm({ ...form, agents: e.target.value })
                      }
                      className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                      placeholder="e.g. 5"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-white/70">
                      Use Case
                    </label>
                    <input
                      required
                      type="text"
                      value={form.useCase}
                      onChange={(e) =>
                        setForm({ ...form, useCase: e.target.value })
                      }
                      className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                      placeholder="e.g. DeFi yield optimizer"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-white/70">
                      Message
                    </label>
                    <textarea
                      rows={4}
                      value={form.message}
                      onChange={(e) =>
                        setForm({ ...form, message: e.target.value })
                      }
                      className="mt-1 w-full rounded-lg border border-white/10 bg-[#0D1117] px-4 py-2.5 text-white placeholder-white/30 focus:border-[#00C9B7] focus:outline-none"
                      placeholder="Tell us more about your project..."
                    />
                  </div>
                  <button
                    type="submit"
                    className="inline-flex w-full items-center justify-center gap-2 rounded-lg bg-[#00C9B7] px-6 py-3 text-sm font-semibold text-black hover:bg-[#00b8a8] transition-colors"
                  >
                    Submit Application
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
