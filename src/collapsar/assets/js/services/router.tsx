import { Layout } from "../pages/Layout";
import { ResourceIndex } from "../pages/ResourceIndex";

import {
  createBrowserRouter,
} from "react-router-dom";
import { ResourceEdit } from "@/pages/ResourceEdit";
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
        element: <ResourceEdit />,
        loader: async ({params}) => {
          return await axios.get(`/collapsar/api/${params.resource}/${params.id}`)
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