"use client";

import { useEffect } from "react";
import posthog from "posthog-js";

// phc_ project tokens are public by design (client-side key); env can override.
const KEY =
  process.env.NEXT_PUBLIC_POSTHOG_KEY ||
  "phc_vppptJACzrhfwphPu3UFDLm7NHzYYByN6nrPs66PCjFx";
const HOST =
  process.env.NEXT_PUBLIC_POSTHOG_HOST || "https://us.i.posthog.com";

export default function PostHogInit() {
  useEffect(() => {
    if (posthog.__loaded) return;
    posthog.init(KEY, {
      api_host: HOST,
      capture_pageview: "history_change", // SPA route changes count as pageviews
      capture_pageleave: true,
      custom_campaign_params: ["ref", "referral"],
      session_recording: { maskAllInputs: true },
      before_send: (event) => {
        const url = event?.properties?.["$current_url"];
        if (typeof url === "string") {
          event!.properties["$current_url"] = url.replace(
            /token=[^&#]+/g,
            "token=[REDACTED]"
          );
        }
        return event;
      },
      loaded: (ph) => {
        if (window.location.hostname === "localhost") ph.opt_out_capturing();
      },
    });
  }, []);
  return null;
}
