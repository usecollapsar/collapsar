import { Label } from "@/components/ui/label";
import { Switch } from "@/components/ui/switch";
import { CheckCircledIcon, CrossCircledIcon } from "@radix-ui/react-icons";
import { boolean } from "zod";

export function BooleanField(props: any) {

  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        {props.value ? <CheckCircledIcon className="text-green-500" /> : <CrossCircledIcon className="text-red-500" />}
      </div>
    );
  };

  if (props.renderForDisplay || !props.fieldConfig) {
    return displayRender();
  }

  const handleOnChange = (e: any) => {
    props.onChange(e.target.checked);
  }

  return (
    <div className="flex items-center space-x-2">
      <Switch
        id={props.attribute}
        checked={props.value}
        onCheckedChange={handleOnChange}
        disabled={props.fieldConfig.readonly}
      />
      <Label htmlFor={props.attribute}>{props.attribute}</Label>
    </div>
  );
}
