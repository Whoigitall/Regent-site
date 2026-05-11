import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import HeroSection from "./components/HeroSection";
import WhySolanaSection from "./components/WhySolanaSection";
import ProductModulesSection from "./components/ProductModulesSection";
import TerminalDemoSection from "./components/TerminalDemoSection";
import LiveMetricsSection from "./components/LiveMetricsSection";
import EventsBanner from "./components/EventsBanner";
import TeamSection from "./components/TeamSection";

export default function Home() {
  return (
    <>
      <Navbar />
      <main className="flex-1">
        <HeroSection />
        <WhySolanaSection />
        <ProductModulesSection />
        <TerminalDemoSection />
        <LiveMetricsSection />
        <EventsBanner />
        <TeamSection />
      </main>
      <Footer />
    </>
  );
}
