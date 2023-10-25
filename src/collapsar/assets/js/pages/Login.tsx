import { ThemeProvider } from "@/components/theme-provider";
import { UserAuthForm } from "@/components/user-auth-form";

export function Login() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="relative min-h-screen flex flex-col items-center justify-center">
        <div className="absolute top-0 left-1 z-20 p-8 flex items-center text-lg font-medium gap-5">
          <img
            className="w-[50px]"
            src="https://avatars.githubusercontent.com/u/148298115?s=200&v=4"
            alt=""
          />
          Collapsar
        </div>

        <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
          <div className="flex flex-col space-y-2 text-center">
            <h1 className="text-2xl font-semibold tracking-tight">Sign in</h1>
            <p className="text-sm text-muted-foreground">
              {/* Enter your credentials below to continue. */}
            </p>
          </div>
          <UserAuthForm />
          <p className="px-8 text-center text-sm text-muted-foreground">

          </p>
        </div>
      </div>
    </ThemeProvider>
  );
}
