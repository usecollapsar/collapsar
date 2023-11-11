import { CalendarIcon } from "@radix-ui/react-icons";
import { format } from "date-fns";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import { FormControl } from "@/components/ui/form";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { useEffect } from "react";

export function CalendarField(props: any) {
  const value = props.value ? new Date(props.value) : new Date();

  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        {props?.value?.toString()}
      </div>
    );
  };

  if (props.renderForDisplay || !props.fieldConfig) {
    return displayRender();
  }

  const handleOnChange = (date: Date) => {
    props.onChange(date);
  }

  // force the value to be a Date object
  useEffect(() => {
    handleOnChange(value);
  }, []);

  return (
    <Popover>
      <PopoverTrigger asChild>
        <FormControl>
          <Button
            variant={"outline"}
            className={cn(
              "w-[240px] pl-3 text-left font-normal",
              !value && "text-muted-foreground"
            )}
          >
            {value ? format(value, "PPP") : <span>Pick a date</span>}
            <CalendarIcon className="ml-auto h-4 w-4 opacity-50" />
          </Button>
        </FormControl>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0" align="start">
        <Calendar
          mode="single"
          selected={value}
          onSelect={handleOnChange}
          // disabled={(date) =>
          //   date > new Date() || date < new Date("1900-01-01")
          // }
          initialFocus
        />
      </PopoverContent>
    </Popover>
  );
}
