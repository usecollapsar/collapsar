import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig(({ mode }) => {
  return {
    build: {
      outDir: "./src/collapsar/dist/assets",
      lib: {
        entry: "./src/collapsar/assets/js/index.tsx",
        formats: ["cjs"],
        fileName: "app-bundle",
      },
    },
    rollupOptions: {
      external: ["react", "react-dom", "react-router-dom"],
      output: {
        globals: {
          react: "React",
          "react-dom": "ReactDOM",
        },
      },
    },
    plugins: [react()],
    define: {
      "process.env.NODE_ENV": JSON.stringify(process.env.NODE_ENV),
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src/collapsar/assets/js/"),
      },
    },
  };
});
