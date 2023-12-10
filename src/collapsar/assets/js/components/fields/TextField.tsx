import { Input } from "@/components/ui/input";

export function TextField({fieldConfig, ...props}: any) {
  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        {props.value.toString()}
      </div>
    );
  };

  if (props.renderForDisplay || !fieldConfig) {
    return displayRender();
  }

  return <Input readOnly={fieldConfig?.readonly} {...props} />;
}
