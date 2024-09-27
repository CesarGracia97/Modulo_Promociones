# Usa la imagen de Node.js apropiada para Angular 17
# Según la documentación, Angular 17 requiere Node.js v18.x
FROM node:18-alpine as build

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo compilado dist.zip al contenedor
COPY dist.zip /app/

# Descomprime el archivo dist.zip
RUN apk add --no-cache unzip && \
    unzip dist.zip -d ./dist && \
    rm dist.zip


 FROM nginx:1.23-alpine

# INSTALAR CERTIFICADOS SSL
# RUN mkdir -p /app/nginx/certs
# COPY certs.zip /app/nginx/certs
# RUN unzip -o /app/nginx/certs/certs.zip -d /app/nginx/certs
    
RUN chgrp -R root /var/cache/nginx /var/run /var/log/nginx && \
    chmod -R 770 /var/cache/nginx /var/run /var/log/nginx
RUN cp /usr/share/zoneinfo/America/Guayaquil /etc/localtime
#COPY default-ssl.conf /etc/nginx/conf.d/default-ssl.conf
COPY nginx.conf /etc/nginx/nginx.conf 
COPY --from=build-step /app/dist/tv-cable-deb-automaticos /usr/share/nginx/html

# Expone el puerto que usarás
EXPOSE 2021