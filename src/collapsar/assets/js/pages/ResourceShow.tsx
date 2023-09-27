import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useLoaderData, useParams } from "react-router-dom";

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
    const fieldInfo = fields.find((f) => f.attribute == field.attribute) as Field;
    const value = data.data[field.attribute];

    return (
      <div className="flex gap-2 flex-col">
        <p>{fieldInfo.name}</p>
        <Input placeholder="" value={value} readonly={true} />
      </div>
    );
  };

  return (
    <>
      <div className="mb-5">
        <h1>{getTitle()}</h1>
      </div>
      <div>
        <form className="space-y-8">
          {fields.map((field) => renderFormField(field))}
        </form>
      </div>
    </>
  );
}
