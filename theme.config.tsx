import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: <span>James' College Notes</span>,
  project: {
    link: 'https://github.com/jamesgwyer/college-notes',
  },
  docsRepositoryBase: 'https://github.com/jamesgwyer/college-notes',
  footer: {
    text: '@jamesgwyer',
  },
  useNextSeoProps() {
    return {
      titleTemplate: '%s – James\' College Notes'
    }
  },
}

export default config
