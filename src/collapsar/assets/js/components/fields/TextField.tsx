import { Input } from "@/components/ui/input";

export function TextField(props: any) {
  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        {props.value.toString()}
      </div>
    );
  };

  if (props.renderForDisplay || !props.fieldConfig) {
    return displayRender();
  }

  return <Input readOnly={props.fieldConfig.readonly} {...props} />;
}
