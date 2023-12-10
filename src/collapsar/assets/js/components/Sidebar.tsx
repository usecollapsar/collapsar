import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Link, usePage, router } from "@inertiajs/react";

export function Sidebar({ className }) {
  const { menuItems } = usePage().props;

  const checkCurrentRoute = (route: string): string => {
    // get current route path from url
    const currentRoute = window.location.pathname;
    return currentRoute == route ? "bg-muted" : "";
  };

  const handleChangeRoute = (route) => {
    router.visit(route);
  };

  return (
    <div className={cn("pb-12", className)}>
      <div className="space-y-4 py-4">
        <div className="px-3 py-2">
          <h2 className="mb-2 px-4 text-lg font-semibold tracking-tight">
            Collapsar
          </h2>
          <div className="space-y-1">
            <Button
              variant={checkCurrentRoute("/")}
              className="w-full justify-start"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="mr-2 h-4 w-4"
              >
                <rect width="7" height="7" x="3" y="3" rx="1" />
                <rect width="7" height="7" x="14" y="3" rx="1" />
                <rect width="7" height="7" x="14" y="14" rx="1" />
                <rect width="7" height="7" x="3" y="14" rx="1" />
              </svg>
              <Link href="/collapsar">Dashboard</Link>
            </Button>
          </div>
        </div>
        {Object.keys(menuItems)?.map((key, k) => (
          <div className="px-3 py-2" key={k}>
            <h2 className="mb-2 px-4 text-lg font-semibold tracking-tight">
              {key}
            </h2>
            <div className="space-y-1 flex flex-col">
              {menuItems[key].map((item, k) => (
                <div
                  key={k}
                  onClick={() => handleChangeRoute("/collapsar/resource/" + item.urikey)}
                  className={`w-full rounded cursor-pointer py-1 px-5 ${checkCurrentRoute(
                    "/collapsar/resource/" + item.urikey
                  )}`}
                >
                  {item.title}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
