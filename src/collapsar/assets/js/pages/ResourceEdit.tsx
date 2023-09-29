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
    let rules = [];

    if (isCreating) {
      rules = field.create_rules.length ? field.create_rules : field.rules;
    } else {
      rules = field.update_rules.length ? field.update_rules : field.rules;
    }

    let schema: z.ZodTypeAny =
      typeof field.value == "number" ? z.number() : z.string();
    let isNullable = false;

    rules.forEach((rule: any) => {
      switch (true) {
        case rule === "required":
          schema = schema.nonempty();
          break;
        case rule.startsWith("max:"):
          schema = schema.max(parseInt(rule.split(":")[1]));
          break;
        case rule.startsWith("min:"):
          schema = schema.min(parseInt(rule.split(":")[1]));
          break;
        case rule === "email":
          schema = schema.email();
          break;
        case rule === "nullable":
          isNullable = true;
          break;
      }
    });

    if (isNullable) {
      const emptyStringOrOriginalSchema = z.union([z.literal(""), schema]);
      schema = emptyStringOrOriginalSchema.nullable().optional();
    }

    createRules[field.attribute] = schema;

    if (!isCreating) {
      defaultValues[field.attribute] = data.data[field.attribute]?.toString();
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
      <FormField
        control={form.control}
        name={field.attribute}
        render={renderForm}
      />
    );
  };

  const renderForm = ({ field }) => {
    const fieldData = fields.find((f) => f.attribute == field.name) as Field;

    const FieldComponent = Fields[fieldData.component as keyof typeof Fields];

    if (!FieldComponent) {
      console.error(`Component ${fieldData.component} not found!`);
      return null;
    }

    return (
      <FormItem className="flex border-b">
        <div className="w-1/4 px-8 py-6">
          <FormLabel>{fieldData.name}</FormLabel>
          <FormDescription>{fieldData.help_text}</FormDescription>
        </div>

        <div className="w-3/4 px-8 py-6">
          <FormControl>
            <FieldComponent fieldConfig={fieldData} {...field} />
          </FormControl>
          <FormMessage />
        </div>
      </FormItem>
    );
  };

  return (
    <>
      <div className="py-4">
        <h1>{getTitle()}</h1>
      </div>
      {form && (
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)}>
            <div className="card rounded border">
              {fields.map((field) => renderFormField(field, form))}
            </div>

            <div className="flex gap-2 mt-6">
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
