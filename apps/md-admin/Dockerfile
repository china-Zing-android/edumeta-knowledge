FROM node:22-alpine AS build

ARG NPM_REGISTRY=https://registry.npmjs.org
ARG VITE_API_BASE_URL=http://127.0.0.1:8000

WORKDIR /app
COPY apps/md-admin/package*.json ./
RUN npm ci --registry="$NPM_REGISTRY"
COPY apps/md-admin/ ./
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL
RUN npm run build

FROM nginx:1.27-alpine
COPY apps/md-admin/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
