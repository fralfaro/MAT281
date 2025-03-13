# Imagen base con Python y algunas herramientas preinstaladas
FROM python:3.10-slim

# Evita la interacción en la instalación de paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Instalar herramientas básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario para VSCode
RUN useradd -ms /bin/bash vscode

# Establecer el directorio de trabajo
WORKDIR /workspace

# Copiar requirements para instalar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto para Jupyter
EXPOSE 8888

# Comando por defecto
CMD ["bash"]
