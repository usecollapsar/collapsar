import { createInertiaApp } from '@inertiajs/react'
import { createRoot } from 'react-dom/client'
import { Layout } from './pages/Layout'

import "../css/app.css"

createInertiaApp({
  resolve: name => {
    const pages = import.meta.glob('./pages/**/*.tsx', { eager: true })
    let page = pages[`./pages/${name}.tsx`]

    page.default.layout = name.startsWith('auth/') ? undefined : page => <Layout children={page} />
    return page
  },
  setup({ el, App, props }) {
    createRoot(el).render(<App {...props} />)
  },
})