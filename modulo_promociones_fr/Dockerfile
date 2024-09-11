FROM node:19.5-alpine as build-step
RUN apk add unzip
RUN apk add --no-cache tzdata
#USER root
RUN mkdir -p /app 
WORKDIR /app

COPY package.json /app
COPY dist.zip /app
#RUN npm install npm@9.4.0
COPY . .
RUN unzip -o /app/dist.zip -d /app/dist
#RUN npm run build --prod

FROM nginx:1.23-alpine

# INSTALAR CERTIFICADOS SSL
RUN mkdir -p /app/nginx/certs
COPY certs.zip /app/nginx/certs
RUN unzip -o /app/nginx/certs/certs.zip -d /app/nginx/certs

RUN chgrp -R root /var/cache/nginx /var/run /var/log/nginx && \
    chmod -R 770 /var/cache/nginx /var/run /var/log/nginx
RUN cp /usr/share/zoneinfo/America/Guayaquil /etc/localtime
#COPY default-ssl.conf /etc/nginx/conf.d/default-ssl.conf
COPY nginx.conf /etc/nginx/nginx.conf 
COPY --from=build-step /app/dist/tv-cable-deb-automaticos /usr/share/nginx/html

EXPOSE 2021
