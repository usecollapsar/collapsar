import { Sidebar } from "../components/Sidebar";
import { useOutlet } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider";
import { Header } from "@/components/Header";

export function Layout() {
  const outlet = useOutlet();

  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <div className="flex">
        <Sidebar />

        <div className="w-full min-h-screen">
          <Header />
          <div className="px-view">
            {outlet || <h1>Nothing to see here</h1>}
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}
