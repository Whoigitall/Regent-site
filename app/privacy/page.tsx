"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import { Shield } from "lucide-react";

export default function PrivacyPage() {
  return (
    <>
      <Navbar />
      <main className="flex-1">
        <section className="w-full bg-black py-20 sm:py-28">
          <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              <Shield className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h1 className="mt-6 text-center text-3xl font-bold text-white sm:text-4xl">
                Privacy Policy
              </h1>
              <p className="mt-4 text-center text-sm text-white/50">
                Last updated: May 2026
              </p>

              <div className="mt-12 space-y-8 text-white/70">
                <div>
                  <h2 className="text-lg font-semibold text-white">1. Introduction</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Regent Protocol (&quot;we&quot;, &quot;our&quot;, &quot;us&quot;) respects your privacy and is committed to protecting your personal data. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or use our services.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">2. Information We Collect</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We may collect the following types of information:
                  </p>
                  <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
                    <li><strong>Personal Information:</strong> Name, email address, company name, and other contact details you provide through forms or correspondence.</li>
                    <li><strong>Usage Data:</strong> Information about how you access and use our website, including IP address, browser type, pages visited, and time spent.</li>
                    <li><strong>Blockchain Data:</strong> Public on-chain data related to AgentID registrations, audit anchors, and transaction hashes. This data is inherently public on the blockchain.</li>
                    <li><strong>Device Information:</strong> Device type, operating system, and unique device identifiers.</li>
                  </ul>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">3. How We Use Your Information</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We use the information we collect for the following purposes:
                  </p>
                  <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
                    <li>To provide, maintain, and improve our services.</li>
                    <li>To communicate with you about updates, support, and marketing (with your consent).</li>
                    <li>To process pilot program applications and verify eligibility.</li>
                    <li>To analyze usage patterns and improve user experience.</li>
                    <li>To comply with legal obligations and enforce our terms.</li>
                  </ul>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">4. Data Sharing and Disclosure</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We do not sell your personal data. We may share information in the following circumstances:
                  </p>
                  <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
                    <li><strong>Service Providers:</strong> With trusted third parties who perform services on our behalf (hosting, analytics, customer support).</li>
                    <li><strong>Legal Requirements:</strong> When required by law, regulation, or legal process.</li>
                    <li><strong>Business Transfers:</strong> In connection with a merger, acquisition, or sale of assets.</li>
                    <li><strong>Consent:</strong> With your explicit consent for specific purposes.</li>
                  </ul>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">5. Blockchain Data</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Data stored on Solana and Celestia blockchains is public and immutable by design. This includes AgentID metadata, audit anchors, and transaction records. We cannot delete or modify on-chain data. Users should be aware that blockchain interactions create permanent, publicly visible records.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">6. Data Security</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We implement industry-standard security measures to protect your personal data, including encryption in transit and at rest, access controls, and regular security audits. However, no method of transmission over the internet or electronic storage is 100% secure.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">7. Your Rights</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Depending on your jurisdiction, you may have the right to:
                  </p>
                  <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
                    <li>Access, correct, or delete your personal data.</li>
                    <li>Object to or restrict processing of your data.</li>
                    <li>Withdraw consent for marketing communications.</li>
                    <li>Request a copy of your data in a portable format.</li>
                  </ul>
                  <p className="mt-2 text-sm leading-relaxed">
                    To exercise these rights, contact us at <a href="mailto:hello@regentprotocol.org" className="text-[#00C9B7] hover:underline">hello@regentprotocol.org</a>.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">8. Cookies and Tracking</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We use cookies and similar technologies to enhance your experience, analyze traffic, and understand user behavior. You can manage cookie preferences through your browser settings. We use analytics services that may set their own cookies.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">9. International Transfers</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Your data may be transferred to and processed in countries other than your country of residence. We ensure appropriate safeguards are in place for such transfers, including standard contractual clauses where required by law.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">10. Changes to This Policy</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We may update this Privacy Policy from time to time. Changes will be posted on this page with an updated revision date. We encourage you to review this policy periodically.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">11. Contact Us</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    If you have questions about this Privacy Policy or our data practices, please contact us at:<br />
                    <a href="mailto:hello@regentprotocol.org" className="text-[#00C9B7] hover:underline">hello@regentprotocol.org</a>
                  </p>
                </div>
              </div>
            </motion.div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
