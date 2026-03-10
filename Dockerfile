# Dockerfile para sitio Hugo estático (ya compilado)
FROM nginx:alpine

# Copiar configuración Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiar archivos HTML estáticos
COPY . /usr/share/nginx/html

EXPOSE 80