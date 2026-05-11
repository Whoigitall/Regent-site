"use client";

import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { motion } from "framer-motion";
import { FileText } from "lucide-react";

export default function TermsPage() {
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
              <FileText className="mx-auto h-10 w-10 text-[#00C9B7]" />
              <h1 className="mt-6 text-center text-3xl font-bold text-white sm:text-4xl">
                Terms of Use
              </h1>
              <p className="mt-4 text-center text-sm text-white/50">
                Last updated: May 2026
              </p>

              <div className="mt-12 space-y-8 text-white/70">
                <div>
                  <h2 className="text-lg font-semibold text-white">1. Acceptance of Terms</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    By accessing or using the Regent Protocol website, dashboard, APIs, or any related services (collectively, the &quot;Services&quot;), you agree to be bound by these Terms of Use. If you do not agree to these terms, do not use the Services.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">2. Eligibility</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    You must be at least 18 years old and capable of entering into legally binding agreements to use our Services. By using the Services, you represent and warrant that you meet these requirements.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">3. Description of Services</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Regent Protocol provides infrastructure for verifying, auditing, and monitoring autonomous AI agents on Solana. This includes AgentID registration, audit chain anchoring, Guardian AI monitoring, and related APIs and dashboards. We reserve the right to modify, suspend, or discontinue any part of the Services at any time.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">4. User Accounts</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    To access certain features, you may need to create an account. You are responsible for maintaining the confidentiality of your account credentials and for all activities under your account. You agree to notify us immediately of any unauthorized use.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">5. Blockchain Interactions</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    Transactions on Solana and Celestia are irreversible. You are solely responsible for verifying transaction details before signing. We are not responsible for lost funds, failed transactions, or smart contract interactions initiated by you.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">6. Prohibited Activities</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    You agree not to:
                  </p>
                  <ul className="mt-2 list-disc space-y-1 pl-5 text-sm">
                    <li>Use the Services for illegal, fraudulent, or unauthorized purposes.</li>
                    <li>Interfere with or disrupt the integrity or performance of the Services.</li>
                    <li>Attempt to gain unauthorized access to any part of the Services or related systems.</li>
                    <li>Reverse engineer, decompile, or disassemble any aspect of the Services.</li>
                    <li>Upload malware, viruses, or other harmful code.</li>
                    <li>Use the Services to create agents that engage in market manipulation or financial crimes.</li>
                  </ul>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">7. Intellectual Property</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    All content, trademarks, logos, and intellectual property on the Services are owned by Regent Protocol or its licensors. You may not reproduce, distribute, or create derivative works without prior written consent. Our open-source SDKs are governed by their respective licenses.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">8. Disclaimer of Warranties</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    THE SERVICES ARE PROVIDED &quot;AS IS&quot; AND &quot;AS AVAILABLE&quot; WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED. WE DO NOT WARRANT THAT THE SERVICES WILL BE UNINTERRUPTED, ERROR-FREE, OR SECURE. BLOCKCHAIN TECHNOLOGY INVOLVES INHERENT RISKS INCLUDING BUT NOT LIMITED TO VOLATILITY, SMART CONTRACT VULNERABILITIES, AND REGULATORY UNCERTAINTY.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">9. Limitation of Liability</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    TO THE MAXIMUM EXTENT PERMITTED BY LAW, REGENT PROTOCOL SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES ARISING OUT OF OR RELATED TO YOUR USE OF THE SERVICES. OUR TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNT YOU PAID TO US IN THE 12 MONTHS PRECEDING THE CLAIM.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">10. Indemnification</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    You agree to indemnify and hold harmless Regent Protocol, its affiliates, officers, directors, employees, and agents from any claims, damages, losses, or expenses arising from your use of the Services or violation of these Terms.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">11. Governing Law</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    These Terms shall be governed by and construed in accordance with the laws of the Republic of Kazakhstan, without regard to its conflict of law provisions. Any disputes shall be resolved in the courts of Almaty, Kazakhstan.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">12. Changes to Terms</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    We may update these Terms from time to time. Material changes will be communicated via email or through the Services. Continued use of the Services after changes constitutes acceptance of the updated Terms.
                  </p>
                </div>

                <div>
                  <h2 className="text-lg font-semibold text-white">13. Contact</h2>
                  <p className="mt-2 text-sm leading-relaxed">
                    For questions about these Terms, contact us at:<br />
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
