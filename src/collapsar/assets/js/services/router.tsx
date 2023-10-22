import { Layout } from "../pages/Layout";
import { ResourceIndex } from "../pages/ResourceIndex";

import {
  createBrowserRouter, useParams,
} from "react-router-dom";
import { ResourceEdit } from "@/pages/ResourceEdit";
import { ResourceShow } from "@/pages/ResourceShow";
import axios from "axios";

// use proxy to remount component on resource change
const ResourceIndexProxy = (props: any) =>
{
  const { resource } = useParams();
  return <ResourceIndex key={resource} {...props} />;
}

const routes = [
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        path: 'resource/:resource',
        element: <ResourceIndexProxy />,
      },
      {
        path: 'resource/:resource/:id',
        element: <ResourceShow />,
        loader: async ({params}) => {
          const res = await axios.get(`/collapsar/api/${params.resource}/${params.id}`)

          return {
            fields: res.data.fields,
            data: res.data.data,
          }
        },
      },
      {
        path: 'resource/:resource/:id/edit',
        element: <ResourceEdit />,
        loader: async ({params}) => {
          const res = await axios.get(`/collapsar/api/${params.resource}/${params.id}`)

          return {
            isCreating: false,
            fields: res.data.fields,
            data: res.data.data,
          }
        },
      },
      {
        path: 'resource/:resource/create',
        element: <ResourceEdit />,
        loader: async ({params}) => {
          const res = await axios.get(`/collapsar/api/${params.resource}/creation-fields`)

          return {
            isCreating: true,
            fields: res.data.fields,
          }
        },
      },
    ]
  },
]

const router = createBrowserRouter(routes,
  {
    basename: "/collapsar",
  }
);

export { router };