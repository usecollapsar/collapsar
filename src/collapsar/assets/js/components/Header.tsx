import { BiUser } from "react-icons/bi"
import { ThemeToggle } from "./ThemeToggle";
import { Button } from "./ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@radix-ui/react-dropdown-menu";

export function Header() {
  const user = window.Collapsar.user

  return (
    <div className="flex p-5">
      <div className="ml-auto header--actions">
        <ThemeToggle />
      </div>
    </div>
  );
}
