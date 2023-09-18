import { Sidebar } from "../components/Sidebar";
import { Outlet } from "react-router-dom";
import { ThemeProvider } from "@/components/theme-provider";

export function Layout() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="flex">
        <Sidebar />
        <div className="px-12 w-full">
          <Outlet />
        </div>
      </div>
    </ThemeProvider>
  );
}
