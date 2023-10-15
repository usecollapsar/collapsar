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
  const onValueChange = (value: any) => {
    props.onChange(value);
  }

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
