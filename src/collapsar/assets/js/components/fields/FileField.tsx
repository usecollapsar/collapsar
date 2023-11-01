import { Input } from "@/components/ui/input";
import { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import { CrossCircledIcon } from "@radix-ui/react-icons";

export function FileField(props: any) {
  const [replaceImage, setReplaceImage] = useState(false);
  const fileInput = useRef<HTMLInputElement>(null);
  const [originalValue, setOriginalValue] = useState(null);

  useEffect(() => {
    setOriginalValue(props.value);
  }, []);

  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2 max-h-[200px]">
        <img className="h-full" src={`/${props.value}`} alt="" />
      </div>
    );
  };

  if (props.renderForIndex) {
    return (
      <div className="flex items-center space-x-2 h-[30px]">
        <img className="h-full" src={`/${props.value}`} alt="" />
      </div>
    );
  }

  if (props.renderForDisplay || !props?.fieldConfig) {
    return displayRender();
  }

  const handleOnChange = (e: any) => {
    props.onChange(e.target.files ? e.target.files[0] : null);
  };

  return (
    <>
      {props.value && !replaceImage ? (
        <div>
          <Button
            type="button"
            variant="secondary"
            onClick={() => setReplaceImage(true)}
          >
            Replace
          </Button>
          <img
            className="rounded-md border-2 mt-3 max-w-sm"
            src={`/${originalValue}`}
            alt=""
          />
        </div>
      ) : (
        <>
          {props.value && (
            <div className="flex flex-col gap-3">
              <div className="flex gap-3">
                <Button
                  type="button"
                  variant="secondary"
                  onClick={(e) => setReplaceImage(false)}
                >
                  Cancel
                </Button>
                <Button
                  type="button"
                  onClick={(e) => fileInput.current?.click()}
                >
                  {fileInput.current?.files?.length > 0 ? "Change selection" : "Select"}
                </Button>
              </div>
              {fileInput.current?.files?.length > 0 ? (
                <div className="text-sm flex flex-col gap-3">
                  <div id="filename">
                    <div className="span">
                      {fileInput.current.files[0].name}{" "}
                    </div>
                    <span className="text-muted-foreground">
                      {(fileInput.current.files[0].size / 1024).toFixed(1)} kb
                    </span>
                  </div>
                  <img
                    className="max-w-[300px]"
                    src={URL.createObjectURL(fileInput.current.files[0])}
                    alt=""
                  />
                </div>
              ) : (
                <span>Choose a file.</span>
              )}
            </div>
          )}

          <Input
            type="file"
            ref={fileInput}
            className="invisible"
            readOnly={props?.fieldConfig.readonly}
            onChange={handleOnChange}
            name={props.name}
          />
        </>
      )}
    </>
  );
}
