"use client";

import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import { Activity, FileCheck, TrendingUp, DollarSign } from "lucide-react";

function useCountUp(target: number, duration = 2000) {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const startTime = Date.now();
    const animate = () => {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);
      setCount(current);
      if (progress < 1) requestAnimationFrame(animate);
    };
    requestAnimationFrame(animate);
  }, [target, duration]);

  return count;
}

const metrics = [
  { icon: Activity, label: "Agents Registered", value: 1247, prefix: "" },
  { icon: FileCheck, label: "Audit Logs Anchored", value: 89234, prefix: "" },
  { icon: TrendingUp, label: "Transactions Processed", value: 456789, prefix: "" },
  { icon: DollarSign, label: "Avg. Cost Per Audit", value: 0, prefix: "$", staticValue: "0.00025" },
];

export default function LiveMetricsSection() {
  return (
    <section className="w-full bg-black py-20 sm:py-28">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-center"
        >
          <h2 className="text-3xl font-bold text-white sm:text-4xl">
            Network Activity
          </h2>
          <p className="mt-3 text-lg text-white/50">
            Live metrics from the Regent Protocol network
          </p>
        </motion.div>

        <div className="mt-14 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {metrics.map((metric, i) => (
            <MetricCard key={metric.label} metric={metric} index={i} />
          ))}
        </div>
      </div>
    </section>
  );
}

function MetricCard({ metric, index }: { metric: typeof metrics[0]; index: number }) {
  const count = useCountUp(metric.value);

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.4, delay: index * 0.08 }}
      className="rounded-lg border border-white/10 bg-[#0D1117] p-6 text-center"
    >
      <metric.icon className="mx-auto h-6 w-6 text-[#00C9B7]" />
      <p className="mt-4 text-2xl font-semibold tabular-nums text-white">
        {metric.staticValue
          ? `${metric.prefix}${metric.staticValue}`
          : `${metric.prefix}${count.toLocaleString()}`}
      </p>
      <p className="mt-1 text-sm text-white/40">{metric.label}</p>
    </motion.div>
  );
}
