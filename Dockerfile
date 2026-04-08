# Dockerfile para sitio Hugo estatico (ya compilado)
FROM nginx:alpine

# Copiar configuracion Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copiar archivos HTML estaticos
COPY . /usr/share/nginx/html

EXPOSE 80
