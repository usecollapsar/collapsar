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
    <Select readOnly={props.fieldConfig.readonly} {...props}>
      <SelectTrigger className="w-[180px]">
        <SelectValue placeholder="Select an option" />
      </SelectTrigger>
      <SelectContent>
        {props.fieldConfig.options.map((option: any, key) => {
          return <SelectItem key={key} value={option?.value?.toString() || option}>{option?.label || option}</SelectItem>;
        })}
      </SelectContent>
    </Select>
  );
}
