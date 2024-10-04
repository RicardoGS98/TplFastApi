# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos y luego instalarlos
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación (por defecto 8000 para FastAPI)
EXPOSE 8000

# Ejecutar las migraciones de Alembic
CMD ["sh", "-c", "alembic upgrade head && gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000"]
