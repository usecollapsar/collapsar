import { Layout } from "../pages/Layout";
import { ResourceIndex } from "../pages/ResourceIndex";

import {
  createBrowserRouter,
} from "react-router-dom";
import { ResourceEdit } from "@/pages/ResourceEdit";
import { ResourceShow } from "@/pages/ResourceShow";
import axios from "axios";


const routes = [
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        path: 'resource/:resource',
        element: <ResourceIndex />,
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