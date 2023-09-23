import { ThemeToggle } from "./ThemeToggle";

export function Header() {
  return (
    <div className="flex p-5">
      <div className="ml-auto header--actions">
        <ThemeToggle />
      </div>
    </div>
  );
}
