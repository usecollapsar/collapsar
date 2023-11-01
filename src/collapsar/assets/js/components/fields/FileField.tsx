import { Input } from "@/components/ui/input";
import { AspectRatio } from "@radix-ui/react-aspect-ratio";
import { useState } from "react";

export function FileField(props: any) {
  const [replaceImage, setReplaceImage] = useState(true);

  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2 max-h-[200px]">
        <img className="h-full" src={`/${props.value}`} alt="" />
      </div>
    );
  };

  if (props.renderForDisplay || !props.fieldConfig) {
    return displayRender();
  }

  const handleOnChange = (e: any) => {
    props.onChange(e.target.files ? e.target.files[0] : null)
  }

  return (
    <>
      {props.value && !replaceImage ? (
        <AspectRatio ratio={5 / 3} className="bg-muted">
          <img className="min-h-full min-w-full" src={props.value} alt="" onClick={() => setReplaceImage(true)} />
        </AspectRatio>
      ) : (
        <Input
          type="file"
          readOnly={props.fieldConfig.readonly}
          onChange={handleOnChange}

          name={props.name}
        />
      )}
    </>
  );
}
