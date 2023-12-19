import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Link } from "@inertiajs/react";

export function BelongsToField(props: any) {
  const onValueChange = (value: any) => {
    props.onChange(value);
  }

  const displayRender = () => {
    return <Link className="text-primary hover:underline" href={`/collapsar/resource/${props.relation_urikey}/${props.value}`}>{props.relation_label}</Link>;
  }

  if (props.renderForDisplay || props.renderForIndex) {
    return displayRender();
  }

  return (
    <Select
      id={props.id}
      onValueChange={onValueChange}
      onBlur={props.onBlur}
      name={props.name}
      disabled={props.disabled}
      defaultValue={props?.value?.toString()}
      ref={props.ref}
    >
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="Select an option" />
      </SelectTrigger>
      <SelectContent>
        {props.fieldConfig.options.map((option: any, key) => {
          return (
            <SelectItem key={key} value={option?.value?.toString() || option}>
              {option?.label || option}
            </SelectItem>
          );
        })}
      </SelectContent>
    </Select>
  );
}
