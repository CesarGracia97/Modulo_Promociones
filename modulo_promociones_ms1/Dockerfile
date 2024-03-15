# Definir la imagen base
FROM python:3.8.10

#Actualizacion de SO e instalacion de herramientas base
RUN apt-get update && apt-get install -y libaio1 unzip 

# Establecer el directorio de trabajo en /app
WORKDIR /usr/src/app

# Copiar los archivos necesarios al contenedor
COPY . /usr/src/app

#Descomprimir la biblioteca de docker e Instalar
RUN unzip /usr/src/app/modulo_promociones_ms1/Config/oracle_client/instantclient-basic-linux.x64-21.8.0.0.0dbru.zip -d /usr/src/app/modulo_promociones_ms1/Config/oracle_client
RUN sh -c "echo /usr/src/app/modulo_promociones_ms1/Config/oracle_client/instantclient_21_8 > \
      /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig
ENV LD_LIBRARY_PATH=/usr/src/app/Modulo-Promociones-backend/modulo_promociones_ms1/Config/oracle_client/nstantclient_21_8

# Actualizar pip
RUN pip install --upgrade pip

# Instalar las dependencias de Python desde requirements.txt
RUN pip install -r /usr/src/app/modulo_promociones_ms1/requirements.txt

# Definir las variables de entorno
ENV O_HOST="192.168.21.165"
ENV O_PORT="1521"
ENV O_SERVICE_NAME="SQL"
ENV O_USERNAME="consulta"
ENV O_PASSWORD="consulta"

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5011

# Comando para ejecutar la aplicación
CMD ["python", "/usr/src/app/modulo_promociones_ms1/__main__.py"]
