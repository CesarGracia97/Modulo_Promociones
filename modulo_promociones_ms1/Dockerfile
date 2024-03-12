# Definir la imagen base
FROM ubuntu:latest

# Mantener el contenedor actualizado
RUN apt-get update && apt-get upgrade -y

# Instalar Python y pip
RUN apt-get install -y python3 python3-pip

# Establecer el directorio de trabajo en /app
WORKDIR /usr/src/app

# Copiar los archivos necesarios al contenedor
COPY . /usr/src/app

# Instalar las dependencias de Python
RUN pip3 install -r requirements.txt

# Definir las variables de entorno
ENV O_HOST="192.168.21.165"
ENV O_PORT="1521"
ENV O_SERVICE_NAME="SQL"
ENV O_USERNAME="consulta"
ENV O_PASSWORD="consulta"


EXPOSE 5010

CMD ["python3", "main.py"]
