# Usar la imagen base de Ubuntu
FROM python:3.8.10

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copiar el contenido del directorio de tu proyecto al contenedor
COPY . /usr/src/app

# Actualizar pip
RUN pip install --upgrade pip

# Instalar las dependencias de Python desde requirements.txt
RUN pip install -r /usr/src/app/modulo_promociones_rapi1/requirements.txt

# Exponer el puerto en el que tu API REST estará escuchando
EXPOSE 5012

# Comando para ejecutar tu aplicación
CMD ["python", "/usr/src/app/modulo_promociones_rapi1/__main__.py"]