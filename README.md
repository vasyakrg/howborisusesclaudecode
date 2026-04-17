# Как Борис использует Claude Code

Сайт с переводом и адаптацией 79 советов от создателя Claude Code — о том, как он использует инструмент ежедневно.

Production: [howborisusesclaudecode.ru](https://howborisusesclaudecode.ru)

## Стек

- **Nuxt 3** (SSR, preset `node-server`)
- **Vue 3** — страницы и компоненты
- Чистый CSS (`assets/css/main.css`), шрифты: JetBrains Mono + Inter
- Контент: статичный JSON (`data/content.ru.json`, `data/volumes.json`)
- Docker + Traefik (labels для HTTPS через Let's Encrypt)

## Структура

```
app.vue                  # корневой layout
nuxt.config.ts           # SSR, meta, шрифты
pages/
  index.vue              # главная — 79 советов
  claudeonomics.vue      # раздел «Клодономика»
components/              # переиспользуемые Vue-компоненты
composables/
  useTerminal.ts         # логика терминального UI
data/
  content.ru.json        # основной контент
  volumes.json           # структура разделов
public/                  # статические ассеты
Dockerfile               # multi-stage build (node:20-alpine)
docker-compose.yml       # деплой за Traefik
```

## Локальная разработка

Требуется Node.js 20+.

```bash
npm install
npm run dev              # http://localhost:3000
```

## Сборка и preview

```bash
npm run build            # сборка в .output
npm run preview          # локальный запуск production-сборки
npm run start            # node .output/server/index.mjs
```

## Деплой

Контейнер собирается из `Dockerfile` (multi-stage), запускается на порту `3000`.
`docker-compose.yml` рассчитан на внешнюю сеть `webproxy` с Traefik — роутинг по хосту `howborisusesclaudecode.ru`, TLS через резолвер `letsEncrypt`.

```bash
docker compose build
docker compose up -d
```

## Переменные окружения

Задаются в `Dockerfile` для runtime-слоя:

- `NODE_ENV=production`
- `HOST=0.0.0.0`, `PORT=3000`
- `NITRO_HOST=0.0.0.0`, `NITRO_PORT=3000`

## Контент

Править тексты советов — `data/content.ru.json`, структуру разделов — `data/volumes.json`. Пересборки образа достаточно для публикации изменений.
