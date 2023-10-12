import { DotsHorizontalIcon } from "@radix-ui/react-icons";
import { Row } from "@tanstack/react-table";
import { AiFillEye } from "react-icons/ai";
import { BiEdit, BiTrash } from "react-icons/bi";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Link, useParams } from "react-router-dom";
import axios from "axios";

interface DataTableRowActionsProps<TData> {
  row: Row<TData>;
}

export function ResourceIndexRowActions<TData>({
  row,
  setData,
}: DataTableRowActionsProps<TData>) {
  const params = useParams();

  const originalField = row.original.find((f) => f.field_name == "IdField");

  const labels = [
    { label: "One", value: 1 },
    { label: "Two", value: 2 },
  ];

  const deleteItem = (row) => {
    axios
      .delete(`/collapsar/api/${params.resource}/${originalField.value}`)
      .then((response) => {
        setData((prevData) => {
          return prevData.filter((item) => item.id != originalField.value);
        });
      });
  };

  return (
    <div className="flex">
      <Button variant="ghost" className="flex h-8 w-8 p-0">
        <Link to={`/resource/${params.resource}/${originalField.value}`}>
          <AiFillEye className="h-4 w-4" />
        </Link>
        <span className="sr-only">View</span>
      </Button>
      <Button variant="ghost" className="flex h-8 w-8 p-0">
        <Link to={`/resource/${params.resource}/${originalField.value}/edit`}>
          <BiEdit className="h-4 w-4" />
        </Link>
        <span className="sr-only">Edit</span>
      </Button>
      <Button
        onClick={() => deleteItem(row)}
        variant="ghost"
        className="flex h-8 w-8 p-0"
      >
        <BiTrash className="h-4 w-4" />
        <span className="sr-only">Delete</span>
      </Button>
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button
            variant="ghost"
            className="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
          >
            <DotsHorizontalIcon className="h-4 w-4" />
            <span className="sr-only">Open menu</span>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end" className="w-[160px]">
          <DropdownMenuItem>Edit</DropdownMenuItem>
          <DropdownMenuItem>Make a copy</DropdownMenuItem>
          <DropdownMenuItem>Favorite</DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuSub>
            <DropdownMenuSubTrigger>Labels</DropdownMenuSubTrigger>
            <DropdownMenuSubContent>
              <DropdownMenuRadioGroup value="2">
                {labels.map((label) => (
                  <DropdownMenuRadioItem key={label.value} value={label.value}>
                    {label.label}
                  </DropdownMenuRadioItem>
                ))}
              </DropdownMenuRadioGroup>
            </DropdownMenuSubContent>
          </DropdownMenuSub>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            Delete
            <DropdownMenuShortcut>⌘⌫</DropdownMenuShortcut>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  );
}
