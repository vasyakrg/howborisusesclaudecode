# syntax=docker/dockerfile:1.7

FROM node:20-alpine AS build
WORKDIR /app
RUN corepack enable
COPY package.json ./
RUN npm install --no-audit --no-fund
COPY . .
RUN npm run build

FROM node:20-alpine AS runtime
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
