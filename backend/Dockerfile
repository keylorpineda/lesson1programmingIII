FROM python:3.12-slim

# Crear usuario no root (opcional)
RUN useradd -m appuser
WORKDIR /app

# Instalar dependencias del sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto
EXPOSE 8000

# Ejecutar con gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
