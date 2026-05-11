"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import { ExternalLink } from "lucide-react";

const teamMembers = [
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
];

export default function TeamSection() {
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
            Building the Future of Agent Compliance
          </h2>
          <p className="mt-4 text-lg text-white/60">
            A team of builders, operators, and strategists united by a mission to make AI agents accountable.
          </p>
        </motion.div>

        <div className="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {teamMembers.map((member, i) => (
            <motion.div
              key={member.name}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.15 }}
              className="group rounded-xl border border-white/10 bg-[#0D1117] p-6 text-center"
            >
              <div className="relative mx-auto h-32 w-32 overflow-hidden rounded-full border-2 border-[#00C9B7]/30">
                <Image
                  src={member.image}
                  alt={member.name}
                  fill
                  className="object-cover"
                />
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
  );
}
