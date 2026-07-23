# syntax=docker/dockerfile:1.7

FROM node:22-alpine AS build
WORKDIR /app
# npm 10.8.x (в node:20-alpine) роняет arborist на дереве Nuxt: "Cannot read
# properties of null (reading 'edgesOut')". Обновляем npm и ставим детерминированно.
RUN npm install -g npm@11
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY . .
RUN npm run build

FROM node:22-alpine AS runtime
WORKDIR /app
ENV NODE_ENV=production \
    NITRO_HOST=0.0.0.0 \
    NITRO_PORT=3000 \
    HOST=0.0.0.0 \
    PORT=3000
COPY --from=build /app/.output ./.output
EXPOSE 3000
USER node
CMD ["node", ".output/server/index.mjs"]
