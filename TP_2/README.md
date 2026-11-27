# Predicción de lluvia en Australia

Trabajo práctico de clasificación de la materia Aprendizaje Automático 1 (Tecnicatura Universitaria en Inteligencia Artificial, FCEIA, UNR).

El objetivo es predecir a las 23:59 de cada día si al día siguiente va a llover en 49 ciudades de Australia, a partir de las mediciones meteorológicas de ese día. El desarrollo completo, con el análisis y las conclusiones, está en el notebook.

## Integrantes

- Franco Esparza
- Franco Renna
- Leandro Picó

## Estructura

```
├── TP-clasificacion-AA1.ipynb   # notebook con el desarrollo y las conclusiones
├── weatherAUS_2026C2.csv        # dataset
├── requirements.txt             # librerías necesarias para el notebook
├── docker/                      # modelo elegido listo para usar con Docker (ver docker/README.md)
└── README.md
```

## Cómo ejecutar el notebook

Se usó **Python 3.11**, porque PyCaret 3.3.2 no funciona con versiones más nuevas. Todos los comandos se ejecutan desde la carpeta del proyecto, donde tienen que estar el notebook y el dataset.

1. Crear el entorno virtual con Python 3.11. En Windows, con el lanzador `py`:

```bash
py -3.11 -m venv .venv
```

En Linux o macOS:

```bash
python3.11 -m venv .venv
```

2. Activarlo.

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

3. Instalar las librerías:

```bash
pip install -r requirements.txt
```

4. Abrir el notebook y ejecutar todas las celdas (Kernel > Restart Kernel and Run All Cells):

```bash
jupyter notebook TP-clasificacion-AA1.ipynb
```

La ejecución completa tarda unos 20 minutos. Las partes más lentas son la imputación con KNN, la búsqueda de hiperparámetros de la red y su explicación con SHAP. La sección 30 vuelve a generar `docker/modelo.joblib` y `docker/lluvia_ejemplo.csv`.

## Cómo ejecutar el Docker

El modelo elegido (la red neuronal optimizada) está listo para usar en la carpeta `docker/`, con todo lo que necesita para predecir sin el notebook y sin conexión a internet. Hace falta tener Docker instalado y abierto, y una terminal de bash (en Windows, Git Bash). Desde la carpeta `docker/`:

```bash
./ejecutar.sh lluvia_ejemplo.csv predicciones.csv
```

El script arma la imagen (`docker build`) y corre el contenedor (`docker run`) con el CSV de entrada, que tiene que tener las columnas originales del dataset y estar en esa carpeta. El resultado, `predicciones.csv`, es el mismo CSV con la probabilidad de lluvia de cada día (`prob_lluvia`) y la predicción (`llueve_manana`). El detalle de los dos comandos y del formato de entrada está en `docker/README.md`.
