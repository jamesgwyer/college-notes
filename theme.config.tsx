import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: <span>James' College Notes</span>,
  project: {
    link: 'https://github.com/jgwyr/college-notes',
  },
  docsRepositoryBase: 'https://github.com/jgwyr/college-notes',
  footer: {
    text: '@jamesgwyer / @jgwyr',
  },
  useNextSeoProps() {
    return {
      titleTemplate: '%s – James\' College Notes'
    }
  },
}

export default config
