import { createContext, useEffect, useState } from "react";
import * as Fields from "@/components/fields";
import { Field } from "@/components/fields/Field";

interface renderFormFieldProps {
  component: string;
  renderForDisplay?: boolean;
  renderForIndex?: boolean;
  field: object;
}

interface CollapsarContextProps {
  renderFormField: (options: renderFormFieldProps) => JSX.Element | null;
  resolveField: (component: string) => typeof Field | null;
}

export const CollapsarContext = createContext({} as CollapsarContextProps);

const CollapsarProvider = ({ children }: any) => {

  const resolveField = (component: any) => {
    const componentName = component.component;

    if (component.custom_field && component.package_name) {
      return window[component.package_name][component.component]
    }

    const fields = import.meta.glob('../components/fields/**/*.tsx', { eager: true })
    const index = Object.keys(fields).findIndex(f => f.split('/').slice(-1)[0] == `${componentName}.tsx`)
    return fields[Object.keys(fields)[index]][componentName]
  }

  const renderFormField = ({
    component,
    field,
    renderForDisplay = false,
    renderForIndex = false,
  }: renderFormFieldProps) => {
    const FieldComponent = resolveField(field);

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
        resolveField,
      }}
    >
      {children}
    </CollapsarContext.Provider>
  );
};

export default CollapsarProvider;
