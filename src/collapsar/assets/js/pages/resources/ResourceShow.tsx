import { Button } from "@/components/ui/button";
// import { Link, useLoaderData, useNavigate, useParams } from "react-router-dom";
import { CollapsarContext } from "@/context/CollapsarProvider";
import { useContext } from "react";
import { usePage, router } from "@inertiajs/react";

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

export default function ResourceShow() {
  const { resource } = usePage().props;
  const { data } = usePage().props;
  // const navigate = useNavigate();
  const { renderFormField } = useContext(CollapsarContext);

  const fields = data.fields;

  const getTitle = () => {
    return `${resource
      ?.charAt(0)
      .toUpperCase()}${resource?.slice(1)} Details`;
  };

  return (
    <>
      <div className="flex">
        <h1>{getTitle()}</h1>
        <Button
          variant="default"
          className="ml-auto"
          onClick={() =>
            router.visit(`/collapsar/resource/${resource}/${data.data.id}/edit`)
          }
        >
          Edit
        </Button>
      </div>
      <div className="py-4">
        <form className="space-y-8 border rounded">
          {fields.map((field, k) => (
            <div key={k} className="flex gap-2 border-b">
              <div className="w-1/4 py-6 px-8">
                <p>{field.name}</p>
              </div>
              {renderFormField({
                component: field.component,
                field,
                renderForDisplay: true,
              })}
            </div>
          ))}
        </form>
      </div>
    </>
  );
}
