import { createContext, useEffect, useState } from "react";
import * as Fields from "@/components/fields";
import axios from "axios";

interface renderFormFieldProps {
  component: string;
  renderForDisplay?: boolean;
  renderForIndex?: boolean;
  field: object;
}

interface CollapsarContextProps {
  renderFormField: (options: renderFormFieldProps) => JSX.Element | null;
}

export const CollapsarContext = createContext({} as CollapsarContextProps);

const CollapsarProvider = ({ children }: any) => {
  const renderFormField = ({
    component,
    field,
    renderForDisplay = false,
    renderForIndex = false,
  }: renderFormFieldProps) => {
    const FieldComponent = Fields[component as keyof typeof Fields];

    if (!FieldComponent) {
      console.error(`Component ${component} not found!`);
      return null;
    }

    return (
      <FieldComponent
        renderForIndex={renderForIndex}
        renderForDisplay={renderForDisplay}
        {...field}
      />
    );
  };

  return (
    <CollapsarContext.Provider
      value={{
        renderFormField,
      }}
    >
      {children}
    </CollapsarContext.Provider>
  );
};

export default CollapsarProvider;
