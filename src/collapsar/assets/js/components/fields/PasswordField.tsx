import { Input } from "@/components/ui/input";

export function PasswordField({fieldConfig, ...props}: any) {
  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        ********
      </div>
    );
  };

  if (props.renderForDisplay || props.renderForIndex) {
    return displayRender();
  }

  return <Input type="password" {...props} />;
}
