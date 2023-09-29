import { Input } from "@/components/ui/input";

export function TextField(props: any) {

  return <Input readOnly={props.fieldConfig.readonly} {...props} />;
}
