import { Sidebar } from "../components/Sidebar";
import { Outlet } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider";
import { Header } from "@/components/Header";

export function Layout() {
  return (
    <ThemeProvider defaultTheme="light" storageKey="vite-ui-theme">
      <div className="flex">
        <Sidebar />

        <div className="w-full">
          <Header />
          <div className="px-view">
            <Outlet />
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}
