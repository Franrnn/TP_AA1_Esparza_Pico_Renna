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
├── requirements.txt             # librerías necesarias
└── README.md
```

## Cómo ejecutarlo

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

La ejecución completa tarda unos 5 minutos. La parte más lenta es la imputación con KNN.
