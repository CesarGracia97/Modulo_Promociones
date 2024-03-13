# Usar la imagen base de Ubuntu
FROM ubuntu:latest

# Actualizar los repositorios e instalar Python 3.12
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar el contenido del directorio de tu proyecto al contenedor
COPY . /usr/src/app

# Instalar las dependencias del proyecto
#RUN pip3 install -r requirements.txt
RUN pip freeze > requirements.txt

# Exponer el puerto en el que tu API REST estará escuchando
EXPOSE 5013

# Comando para ejecutar tu aplicación
CMD ["python3",  "0.0.0.0:5013", "main.py"]