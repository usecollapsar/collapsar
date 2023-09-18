import '../css/app.scss'
import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {router} from "./services/router";

import {
  RouterProvider,
} from "react-router-dom";


ReactDOM.createRoot(document.getElementById("collapsar")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);