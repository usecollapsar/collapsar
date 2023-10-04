import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"

export function BooleanField(props: any) {
  return (
    <div className="flex items-center space-x-2">
      <Switch 
      id={props.attribute} 
      checked={props.value}
      onCheckedChange={props.onChange}
      disabled={props.fieldConfig.readonly} />
      <Label htmlFor={props.attribute}>{props.attribute}</Label>
    </div>
  )
}