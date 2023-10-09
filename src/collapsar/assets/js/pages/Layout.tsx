import { Sidebar } from "../components/Sidebar";
import { useOutlet } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider";
import { Header } from "@/components/Header";
import { Dashboard } from "@/components/Dashboard";

export function Layout() {
  const outlet = useOutlet();

  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <div className="flex">
        <Sidebar />

        <div className="w-full min-h-screen">
          <Header />
          <div className="px-view">
            {outlet || <Dashboard />}
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}
