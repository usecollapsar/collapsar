import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Link, useLoaderData, useNavigate, useParams } from "react-router-dom";
import * as Fields from "@/components/fields";

type Field = {
  id: number | string;
  name: string;
  type: string;
  required: boolean;
  component: string;
  attribute: string;
  help_text: string;
  value: string | number;
};

interface RouterResponse {
  data?: any;
  fields: [Field];
  isCreating: Boolean;
}

export function ResourceShow() {
  const params = useParams();
  const data = useLoaderData() as RouterResponse;
  const navigate = useNavigate();

  const fields = data.fields;

  const getTitle = () => {
    return `${params?.resource
      ?.charAt(0)
      .toUpperCase()}${params?.resource?.slice(1)} Details`;
  };

  const renderFormField = (field: Field) => {
    const fieldData = fields.find(
      (f) => f.attribute == field.attribute
    ) as Field;

    const FieldComponent = Fields[fieldData.component as keyof typeof Fields];

    if (!FieldComponent) {
      console.error(`Component ${fieldData.component} not found!`);
      return null;
    }

    return (
      <div className="flex gap-2 border-b">
        <div className="w-1/4 py-6 px-8">
          <p>{fieldData.name}</p>
        </div>
        <FieldComponent renderForDisplay={true} {...field} />
      </div>
    );
  };

  return (
    <>
      <div className="flex">
        <h1>{getTitle()}</h1>
        <Button variant="default" className="ml-auto" onClick={() => navigate(`/resource/${params.resource}/${data.data.id}/edit`)}>
            Edit
        </Button>
      </div>
      <div className="py-4">
        <form className="space-y-8 border rounded">
          {fields.map((field) => renderFormField(field))}
        </form>
      </div>
    </>
  );
}
