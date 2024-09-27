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

# Instala un servidor HTTP simple para servir el contenido estático de Angular
RUN npm install -g http-server

# Fase para instalar certificados SSL
# Copia y descomprime certs.zip
COPY certs.zip /app/
RUN unzip certs.zip -d /etc/ssl/certs/ && \
    rm certs.zip

# Expone el puerto que usarás
EXPOSE 2021

# Comando para correr la aplicación con http-server
CMD ["http-server", "dist", "-p", "2021", "--ssl", "--cert", "/etc/ssl/certs/cert.pem", "--key", "/etc/ssl/certs/key.pem"]
