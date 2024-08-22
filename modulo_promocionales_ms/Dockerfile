FROM python:3.10-slim-buster

# Configurar hora correcta servidor
ENV TZ=America/Guayaquil

# Actualiza e instala paquetes necesarios OS
RUN apt-get update \
&& apt-get install -y libaio1 unzip \
&& rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /usr/src/app

# Crear carpeta logs
RUN mkdir -p /usr/src/app /usr/src/app/logs

# Copiar archivos al contenedor
COPY . /usr/src/app

# Instalar librerias ORACLE
RUN unzip /usr/src/app/swagger_server/config/oracle_client/instantclient-basic-linux.x64-21.8.0.0.0dbru.zip -d /usr/src/app/swagger_server/config/oracle_client
RUN sh -c "echo /usr/src/app/swagger_server/config/oracle_client/instantclient_21_8 > \
      /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig
ENV LD_LIBRARY_PATH=/usr/src/app/swagger_server/config/oracle_client/instantclient_21_8

# Instalar librerias PYTHON
COPY requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


# Exponer el puerto
EXPOSE 2013

# ------------------------ SERVIDOR PRODUCCION ------------------------
# timeout - Tiempo en segundos para no detener el request si se demora mas
# worker-class - Tipo de worker: sync (sincronica), gevent o eventlet (asincrono)
# workers -  Cantidad de procesos para manejar peticiones concurrentes (por defecto en desarrollo es 1)
# bind - ip:puerto exponer el servicio
# worker-connections - Peticiones simultaneas
# CMD para ejecutar la aplicación
CMD ["gunicorn", "--workers=3", "--bind","0.0.0.0:2013", "--worker-class=sync", "--timeout=300", "swagger_server.__main__:create_app()"]