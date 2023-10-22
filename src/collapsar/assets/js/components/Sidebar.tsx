import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Link, useLocation, useNavigate, useSearchParams } from "react-router-dom";

export function Sidebar({ className }) {
  const menuItems = window.Collapsar.sidebar.items;
  const location = useLocation();
  const navigate = useNavigate();

  const checkCurrentRoute = (route) => {
    return route == location.pathname ? "secondary" : "ghost";
  };

  const handleChangeRoute = (route) => {
    navigate({pathname: route}, { replace: true });
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
              <Link to="/">Dashboard</Link>
            </Button>
          </div>
        </div>
        {Object.keys(menuItems)?.map((key) => (
          <div className="px-3 py-2">
            <h2 className="mb-2 px-4 text-lg font-semibold tracking-tight">
              {key}
            </h2>
            <div className="space-y-1">
              {menuItems[key].map((item, k) => (
                <Button
                  key={k}
                  variant={checkCurrentRoute("/resource/" + item.urikey)}
                  className="w-full justify-start"
                  onClick={() => handleChangeRoute("/resource/" + item.urikey)}
                >
                  {item.title}
                </Button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
