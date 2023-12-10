import { Input } from "@/components/ui/input";

export interface FieldProps {
  renderForIndex?: boolean;
  renderForDisplay?: boolean;
  fieldConfig?: any;
  name?: string;
  type?: string;
  value?: any;
  required?: boolean;
  component?: string;
  attribute?: string;
  help_text?: string;
}

export function Field(props: FieldProps) {

  return (
    <>
    <Input />
    </>
  )
}