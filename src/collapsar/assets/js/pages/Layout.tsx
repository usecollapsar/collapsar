import { Sidebar } from "../components/Sidebar";
import { useOutlet } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider";
import { Header } from "@/components/Header";
import { Dashboard } from "@/components/Dashboard";
import CollapsarProvider from "@/context/CollapsarProvider";


export function Layout() {
  const outlet = useOutlet();

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <CollapsarProvider>
      <div className="flex">
        <Sidebar />

        <div className="w-full min-h-screen">
          <Header />
          <div className="px-view">
            {outlet || <Dashboard />}
          </div>
        </div>
      </div>
      </CollapsarProvider>
    </ThemeProvider>
  );
}
