FROM docker.m.daocloud.io/library/node:20-slim AS build

ARG NPM_REGISTRY=https://registry.npmmirror.com

WORKDIR /app
COPY apps/tool-gateway/package.json /app/package.json
COPY apps/tool-gateway/package-lock.json /app/package-lock.json

RUN npm ci --registry="$NPM_REGISTRY"

COPY apps/tool-gateway/src /app/src
COPY apps/tool-gateway/test /app/test
COPY apps/tool-gateway/tsconfig.json /app/tsconfig.json

RUN npm run build

FROM docker.m.daocloud.io/library/node:20-slim AS production

ARG NPM_REGISTRY=https://registry.npmmirror.com

ENV NODE_ENV=production
WORKDIR /app

COPY apps/tool-gateway/package.json /app/package.json
COPY apps/tool-gateway/package-lock.json /app/package-lock.json
RUN npm ci --omit=dev --registry="$NPM_REGISTRY" && npm cache clean --force

COPY --from=build /app/dist/src /app/dist/src

USER node
CMD ["node", "dist/src/server.js"]
