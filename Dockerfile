# Dockerfile para Blog Hugo con EasyPanel
FROM hugomods/hugo:exts-0.136.5 AS builder

WORKDIR /src
COPY . .

# Build del sitio estático
RUN hugo --minify --gc --environment production

# Servidor web con Nginx (más liviano que Caddy para static files)
FROM nginx:alpine

# Copiar archivos generados
COPY --from=builder /src/public /usr/share/nginx/html

# Configuración nginx optimizada
RUN echo 'server { \
    listen 80; \
    root /usr/share/nginx/html; \
    index index.html; \
    \
    location / { \
        try_files $uri $uri/ $uri.html /index.html; \
    } \
    \
    location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg|woff|woff2|ttf|eot)$ { \
        expires 1y; \
        add_header Cache-Control "public, immutable"; \
    } \
    \
    gzip on; \
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript; \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80