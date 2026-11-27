# Misma versión de Python con la que se entrenó el modelo
FROM python:3.11-slim

WORKDIR /app

# Primero las librerías, así Docker reutiliza esta capa si solo cambia el script o el modelo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inferencia.py modelo.joblib ./

ENTRYPOINT ["python", "inferencia.py"]
