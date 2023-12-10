import * as React from "react"

import { router, useForm } from "@inertiajs/react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { FaSpinner } from "react-icons/fa6";

interface UserAuthFormProps extends React.HTMLAttributes<HTMLDivElement> {}

export function UserAuthForm({ className, ...props }: UserAuthFormProps) {
  const [isLoading, setIsLoading] = React.useState<boolean>(false)
  const { data, setData, post, transform, processing, errors } = useForm({
    email: "",
    password: "",
  });

  async function onSubmit(event: React.SyntheticEvent) {
    event.preventDefault()

    post("/collapsar/auth/login", data)
  }

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target
    setData({
      ...data,
      [name]: value,
    })
  }

  return (
    <div className={cn("grid gap-6", className)} {...props}>
      <form onSubmit={onSubmit}>
        <div className="grid gap-5">
          <div className="grid gap-3">
            <Label htmlFor="email">
              Email address
            </Label>
            <Input
              id="email"
              name="email"
              placeholder=""
              type="email"
              onChange={handleChange}
              autoCapitalize="none"
              autoComplete="email"
              autoCorrect="off"
              disabled={processing}
            />
          </div>
          <div className="grid gap-3">
            <Label htmlFor="password">
              Password
            </Label>
            <Input
              id="password"
              name="password"
              placeholder=""
              type="password"
              onChange={handleChange}
              autoCapitalize="none"
              autoComplete="none"
              autoCorrect="off"
              disabled={processing}
            />
          </div>
          <div className="text-red-500">
          {errors?.global}
          </div>
          <Button disabled={processing}>
            {isLoading && (
              <FaSpinner className="mr-2 h-4 w-4 animate-spin" />
            )}
            Sign In with Email
          </Button>
        </div>
      </form>
    </div>
  )
}
