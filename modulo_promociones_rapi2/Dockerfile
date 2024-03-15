# Usar la imagen base de Ubuntu
FROM python:3.8.10

# Actualizar los repositorios e instalar Python 3.12
RUN apt-get update 

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar el contenido del directorio de tu proyecto al contenedor
COPY . /usr/src/app

# Instalar las dependencias del proyecto
RUN pip install -r /usr/src/app/modulo_promociones_rapi2/requirements.txt


# Exponer el puerto en el que tu API REST estará escuchando
EXPOSE 5013

# Comando para ejecutar tu aplicación
CMD ["python", "/usr/src/app/modulo_promociones_rapi2/__main__.py"]