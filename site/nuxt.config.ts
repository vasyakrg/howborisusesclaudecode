export default defineNuxtConfig({
  compatibilityDate: '2025-10-01',
  ssr: true,
  nitro: {
    preset: 'node-server'
  },
  app: {
    head: {
      htmlAttrs: { lang: 'ru' },
      title: 'Как Борис использует Claude Code',
      meta: [
        { charset: 'UTF-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
        { name: 'description', content: '79 советов от создателя Claude Code о том, как он использует его ежедневно' },
        { property: 'og:title', content: 'Как Борис использует Claude Code' },
        { property: 'og:description', content: '79 советов от создателя Claude Code' },
        { property: 'og:type', content: 'website' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap' }
      ],
      script: [
        {
          src: 'https://umami.bildme.ru/script.js',
          defer: true,
          'data-website-id': '077e77d0-ad24-46ce-8b38-e6636fec08b8'
        }
      ]
    }
  },
  css: ['~/assets/css/main.css']
})
