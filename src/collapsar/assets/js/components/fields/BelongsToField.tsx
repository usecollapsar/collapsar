import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

export function BelongsToField(props: any) {
  const onValueChange = (value: any) => {
    props.onChange(value);
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
