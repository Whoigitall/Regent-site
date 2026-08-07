import { homeFaqs } from "../home-faqs";

// Server component — static, so the Q&A live directly in the HTML (best for SEO
// and AI answer engines). The FAQPage schema is generated from the same array
// rendered below, so structured data always mirrors the visible content.
const faqLd = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: homeFaqs.map((f) => ({
    "@type": "Question",
    name: f.question,
    acceptedAnswer: { "@type": "Answer", text: f.answer },
  })),
};

export default function FaqSection() {
  return (
    <section className="w-full bg-black py-20 sm:py-28">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqLd) }}
      />
      <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-center text-3xl font-bold text-white sm:text-4xl">
          Frequently Asked Questions
        </h2>
        <p className="mt-4 text-center text-lg text-white/60">
          The essentials on Know Your Agent, spending controls, and agent identity.
        </p>
        <dl className="mt-12 space-y-6">
          {homeFaqs.map((f) => (
            <div
              key={f.question}
              className="rounded-xl border border-white/10 bg-white/[0.02] p-6"
            >
              <dt className="text-lg font-semibold text-white">{f.question}</dt>
              <dd className="mt-3 leading-relaxed text-white/60">{f.answer}</dd>
            </div>
          ))}
        </dl>
      </div>
    </section>
  );
}
