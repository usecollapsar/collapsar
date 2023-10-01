import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

export function SelectField(props: any) {
  return (
    <Select
      id={props.id}
      onValueChange={props.onChange}
      onBlur={props.onBlur}
      name={props.name}
      disabled={props.disabled}
      defaultValue={props.value}
      ref={props.ref}
    >
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="Select an option" />
      </SelectTrigger>
      <SelectContent>
        {props.fieldConfig.options.map((option: any, key) => {
          return (
            <SelectItem key={key} value={option?.label || option}>
              {option?.label || option}
            </SelectItem>
          );
        })}
      </SelectContent>
    </Select>
  );
}
