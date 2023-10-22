import { createContext, useEffect, useState } from "react";
import * as Fields from "@/components/fields";

interface renderFormFieldProps {
  component: string;
  renderForDisplay?: boolean;
  field: object;
}

interface CollapsarContextProps {
  renderFormField: (options: renderFormFieldProps) => JSX.Element;
}

export const CollapsarContext = createContext({} as CollapsarContextProps);

const CollapsarProvider = ({ children }: any) => {

  const renderFormField = ({component, field, renderForDisplay = false}: renderFormFieldProps) => {
    const FieldComponent = Fields[component as keyof typeof Fields];

    if (!FieldComponent) {
      console.error(`Component ${component} not found!`);
      return null;
    }

    return (
      <FieldComponent renderForDisplay={true} {...field} />
    );

  }


  return (
    <CollapsarContext.Provider
      value={{
        renderFormField
      }}
    >
      {children}
    </CollapsarContext.Provider>
  );
};

export default CollapsarProvider;
