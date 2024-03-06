import CodeMirror from "@uiw/react-codemirror";
import { vscodeDark } from "@uiw/codemirror-theme-vscode";
import { markdown } from "@codemirror/lang-markdown";

export function MarkdownField({fieldConfig, ...props}: any) {
  const displayRender = () => {
    return (
      <div className="flex items-center space-x-2">
        {props.value.toString()}
      </div>
    );
  };

  if (props.renderForDisplay || props.renderForIndex) {
    // return displayRender();
  }

  return <CodeMirror
  onChange={(value) => props.onChange(value)}
  className=""
  height=""
  readOnly={props.renderForDisplay || props.renderForIndex}
  theme={vscodeDark}
  value={props.value}
  extensions={[markdown()]}
/>

}
