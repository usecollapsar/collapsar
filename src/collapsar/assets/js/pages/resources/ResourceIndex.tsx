import axios from "axios";
import * as React from "react";
import { CaretSortIcon, ChevronDownIcon } from "@radix-ui/react-icons";

import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";

import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
// import { Link, useNavigate, useParams, useSearchParams } from "react-router-dom";

import { ResourceIndexRowActions } from "@/components/ResourceIndexRowActions";
import { CollapsarContext } from "@/context/CollapsarProvider";
import { usePage, router } from "@inertiajs/react";

export default function ResourceIndex() {
  const { resource } = usePage().props;
  const { renderFormField } = React.useContext(CollapsarContext);

  const [data, setData] = React.useState([]);
  const [meta, setMeta] = React.useState({} as any);
  const [fields, setFields] = React.useState([]);
  const [sorting, setSorting] = React.useState<SortingState>([]);
  // const [searchParams, setSearchParams] = useSearchParams()
  const [searchString, setSearchString] = React.useState('')

  const [pagination, setPagination] = React.useState({
    pageIndex: 0,
    pageSize: 10,
  });

  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  );
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({});
  const [rowSelection, setRowSelection] = React.useState({});

  const handlePagination = ({ page }) => {
    const sortBy = sorting?.[0].id ?? ""
    const sortDesc = sorting?.[0].desc

    axios.get(`/collapsar-api/${resource}`, {params: { search: searchString, page: page + 1, sort_by: sortBy, sort_desc: sortDesc }})
    .then((response) => {
      setData(response.data.data);
      setFields(response.data.fields);
      setMeta(response.data.meta);
    });
  };

  const constructColumns = (fields: any[]): ColumnDef[any] => {
    const columns = fields.map((field, k) => {
      return {
        id: field.attribute,
        accessorKey: field.name,
        header: ({ column }) => {
          return (
            <Button
              variant="ghost"
              onClick={() =>
                column.toggleSorting(column.getIsSorted() === "asc")
              }
            >
              {field.name.toUpperCase()}
              <CaretSortIcon className="ml-2 h-4 w-4" />
            </Button>
          );
        },
        cell: ({ row }) => {
          const originalField = row.original[k];
          return renderFormField({ component: originalField.component, field: originalField, renderForIndex: true})
        },
      };
    });

    return [
      {
        id: "select",
        header: ({ table }) => (
          <Checkbox
            checked={table.getIsAllPageRowsSelected()}
            onCheckedChange={(value) =>
              table.toggleAllPageRowsSelected(!!value)
            }
            aria-label="Select all"
          />
        ),
        cell: ({ row }) => (
          <Checkbox
            checked={row.getIsSelected()}
            onCheckedChange={(value) => row.toggleSelected(!!value)}
            aria-label="Select row"
          />
        ),
        enableSorting: true,
        enableHiding: true,
      },
      ...columns,
      {
        id: "actions",
        cell: ({ row }) => (
          <ResourceIndexRowActions row={row} setData={setData} />
        ),
      },
    ];
  };

  const columns = constructColumns(fields);
  // const navigate = useNavigate();

  const table = useReactTable({
    data: data,
    columns,
    manualPagination: true,
    manualSorting: true,
    onPaginationChange: setPagination,
    pageCount: meta.last_page,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
      pagination,
    },
  });

  // React.useEffect(() => {
  //   // setSearchParams(`?${new URLSearchParams({ page: table.getState().pagination.pageIndex + 1 })}`)
  // }, [pagination]);

  React.useEffect(() => {
    console.log(sorting)
    handlePagination({ page: table.getState().pagination.pageIndex });
  }, [pagination, resource, sorting, searchString]);

  return (
    <div className="w-full">
      <h1 className="font-bold text-3xl">{meta?.resource?.title}</h1>

      <div className="flex items-center py-4">
        <Input
          placeholder="Search"
          value={searchString}
          onChange={(event) =>
            setSearchString(event.target.value)
          }
          className="max-w-sm"
        />
        <Button
          variant="default"
          className="ml-auto"
          onClick={() => router.visit(`/collapsar/resource/${resource}/create`)}
        >
          Create
        </Button>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-5">
              Columns <ChevronDownIcon className="ml-2 h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter((column) => column.getCanHide())
              .map((column) => {
                return (
                  <DropdownMenuCheckboxItem
                    key={column.id}
                    className="capitalize"
                    checked={column.getIsVisible()}
                    onCheckedChange={(value) =>
                      column.toggleVisibility(!!value)
                    }
                  >
                    {column.id}
                  </DropdownMenuCheckboxItem>
                );
              })}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <div className="rounded-md border">
        <Table className="text-md">
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => {
                  return (
                    <TableHead key={header.id}>
                      {header.isPlaceholder
                        ? null
                        : flexRender(
                            header.column.columnDef.header,
                            header.getContext()
                          )}
                    </TableHead>
                  );
                })}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  data-state={row.getIsSelected() && "selected"}
                >
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
                      {flexRender(
                        cell.column.columnDef.cell,
                        cell.getContext()
                      )}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={columns.length}
                  className="h-24 text-center"
                >
                  No results.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
      <div className="flex items-center justify-end space-x-2 py-4">
        <div className="flex-1 text-sm text-muted-foreground">
          {table.getFilteredSelectedRowModel().rows.length} of{" "}
          {table.getFilteredRowModel().rows.length} row(s) selected.
        </div>

        <div className="flex-1 text-sm text-muted-foreground">
              Page {table.getState().pagination.pageIndex + 1} of{" "} {meta.last_page}
        </div>
        <div className="space-x-2">
          <Button
            variant="outline"
            size="sm"
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
          >
            Previous
          </Button>
          <Button
            variant="outline"
            size="sm"
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
          >
            Next
          </Button>
        </div>
      </div>
    </div>
  );
}
