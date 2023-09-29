import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Link, useLoaderData, useParams } from "react-router-dom";

type Field = {
  id: number | string;
  name: string;
  type: string;
  required: boolean;
  attribute: string;
  help_text: string;
};

interface RouterResponse {
  data?: any;
  fields: [Field];
  isCreating: Boolean;
}

export function ResourceShow() {
  const params = useParams();
  const data = useLoaderData() as RouterResponse;

  const fields = data.fields;

  const getTitle = () => {
    return `${params?.resource
      ?.charAt(0)
      .toUpperCase()}${params?.resource?.slice(1)} Details`;
  };

  const renderFormField = (field: Field) => {
    const fieldInfo = fields.find(
      (f) => f.attribute == field.attribute
    ) as Field;
    const value = data.data[field.attribute];

    if (!value) return null;

    return (
      <div className="flex gap-2 border-b">
        <div className="w-1/4 py-6 px-8">
          <p>{fieldInfo.name}</p>
        </div>
        <div className="w-3/4 py-6 px-8">
          <Input placeholder="" value={value} readonly={true} />
        </div>
      </div>
    );
  };

  return (
    <>
      <div className="flex">
        <h1>{getTitle()}</h1>
        <Button variant="default" className="ml-auto">
          <Link to={`/resource/${params.resource}/${data.data.id}/edit`}>
            Edit
          </Link>
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
