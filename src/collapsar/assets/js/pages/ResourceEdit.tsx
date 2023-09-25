import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { useForm } from "react-hook-form";
import { Link, useLoaderData, useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import * as Fields from "@/components/fields";

type Field = {
  id: number | string;
  name: string;
  type: string;
  required: boolean;
  component: string;
  attribute: string;
  help_text: string;
};

interface RouterResponse {
  data?: any;
  fields: [Field];
  isCreating: Boolean;
  resource_model: object;
}

interface FieldValues {
  [key: string]: string;
}

export function ResourceEdit() {
  const params = useParams();
  const data = useLoaderData() as RouterResponse;
  let navigate = useNavigate();

  const isCreating = data.isCreating;
  const fields = data.fields;
  let defaultValues: FieldValues = {};
  let createRules: any = {};

  fields.forEach((field: any) => {
    let fieldRules = z.any();

    field.rules.forEach((rule: any) => {
      if (rule.name == "required") {
        fieldRules = fieldRules.nonempty({
          message: `${field.name} is required.`,
        });
      }

      if (rule.name == "max") {
        fieldRules = fieldRules.max(rule.args[0], {
          message: `${field.name} must be less than ${rule.args[0]}.`,
        });
      }
    });

    createRules[field.name] = fieldRules;

    if (!isCreating) {
      defaultValues[field.name] = data.data[field.name];
    }
  });

  const createSchema = z.object(createRules);

  const form = useForm<z.infer<typeof createSchema>>({
    resolver: zodResolver(createSchema),
    defaultValues,
  });

  function onSubmit(values: any) {
    if (isCreating) {
      return axios
        .put(`/collapsar/api/${params.resource}/`, values)
        .then((response) => {
          console.log("Success");
          console.log(response.data);

          navigate(
            `/resource/${params.resource}/${response.data.resource_model.id}`
          );
        });
    }

    axios
      .patch(`/collapsar/api/${params.resource}/${data.data.id}`, values)
      .then((response) => {
        console.log("Success");
        console.log(response.data);

        navigate(`/resource/${params.resource}/${response.data.resource.id}`);
      });
  }

  const getTitle = () => {
    if (isCreating) {
      return `Create ${params.resource
        ?.charAt(0)
        .toUpperCase()}${params.resource?.slice(1)}`;
    }

    return `Update ${params.resource
      ?.charAt(0)
      .toUpperCase()}${params.resource?.slice(1)}`;
  };

  const renderFormField = (field: Field, form) => {
    return (
      <FormField control={form.control} name={field.name} render={renderForm} />
    );
  };

  const renderForm = ({ field }) => {
    const fieldData = fields.find((f) => f.name == field.name) as Field;

    const FieldComponent = Fields[fieldData.component as keyof typeof Fields];

    if (!FieldComponent) {
      console.error(`Component ${fieldData.component} not found!`);
      return null; 
    }

    return (
      <FormItem>
        <FormLabel>{fieldData.attribute}</FormLabel>
        <FormControl>
          <FieldComponent {...field} />
        </FormControl>
        <FormDescription>{fieldData.help_text}</FormDescription>
        <FormMessage />
      </FormItem>
    );
  };

  return (
    <>
      <div className="mb-5">
        <h1>{getTitle()}</h1>
      </div>
      {form && (
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            {fields.map((field) => renderFormField(field, form))}

            <div className="flex gap-2">
              <Button variant="secondary">
                <Link to={`/resource/${params.resource}`}>Cancel</Link>
              </Button>
              <Button type="submit">{isCreating ? "Create" : "Update"}</Button>
            </div>
          </form>
        </Form>
      )}
    </>
  );
}
