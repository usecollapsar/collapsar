import { Sidebar } from "../components/Sidebar";
import { ThemeProvider } from "@/components/theme-provider";
import { Header } from "@/components/Header";
import CollapsarProvider from "@/context/CollapsarProvider";


export function Layout({children}) {
  // const outlet = useOutlet();

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <CollapsarProvider>
      <div className="flex">
        <Sidebar />

        <div className="w-full min-h-screen">
          <Header />
          <div className="px-view">
            {children}
          </div>
        </div>
      </div>
      </CollapsarProvider>
    </ThemeProvider>
  );
}
