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
import { Link, useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import { AlertMessage } from "./utils/AlertMessage";
import { useState } from "react";

interface DataTableRowActionsProps<TData> {
  row: Row<TData>;
}

export function ResourceIndexRowActions<TData>({
  row,
  setData,
}: DataTableRowActionsProps<TData>) {
  const params = useParams();
  const navigate = useNavigate();
  const [alertMessageOpen, setAlertMessageOpen] = useState(false);
  const [alertMessageTitle, setAlertMessageTitle] = useState('');
  const [alertMessageContent, setAlertMessageContent] = useState('');
  const [selectedRow, setSelectedRow] = useState(null);

  const originalField = row.original.find((f) => f.field_name == "Id");

  const labels = [
    { label: "One", value: 1 },
    { label: "Two", value: 2 },
  ];

  const openDeleteAlert = (row) => {
    setAlertMessageTitle('Delete');
    setAlertMessageContent('Are you sure you want to delete this item?');
    setAlertMessageOpen(true);
    setSelectedRow(row)
  }

  const deleteItem = (row) => {
    axios
      .delete(`/collapsar/api/${params.resource}/${originalField.value}`)
      .then((response) => {
        setData((prevData) => {
          return prevData.filter((item) => {
            return !item.some(f => f.primary_key && f.value == originalField.value)
          });
        });
      });
  };

  return (
    <div className="flex">
      <AlertMessage open={alertMessageOpen} setOpen={setAlertMessageOpen} title={alertMessageTitle} content={alertMessageContent} onConfirm={() => deleteItem(selectedRow)} />
      <Button
        variant="ghost"
        className="flex h-8 w-8 p-0"
        onClick={() =>
          navigate(`/resource/${params.resource}/${originalField.value}`)
        }
      >
        <AiFillEye className="h-4 w-4" />
        <span className="sr-only">View</span>
      </Button>
      <Button
        variant="ghost"
        className="flex h-8 w-8 p-0"
        onClick={() =>
          navigate(`/resource/${params.resource}/${originalField.value}/edit`)
        }
      >
        <BiEdit className="h-4 w-4" />
        <span className="sr-only">Edit</span>
      </Button>
      <Button
        onClick={() => openDeleteAlert(row)}
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
