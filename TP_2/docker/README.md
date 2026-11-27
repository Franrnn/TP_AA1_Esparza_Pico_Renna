# Predicción de lluvia con Docker

Imagen de Docker que predice si mañana va a llover a partir de las mediciones de un día. Usa la red neuronal elegida en el notebook (`TP-clasificacion-AA1.ipynb`, ítem 8). No necesita conexión a internet: todo lo que usa, incluida la tabla de coordenadas de las ciudades, viene dentro de `modelo.joblib`.

## Contenido de la carpeta

```
docker/
├── Dockerfile            # receta para armar la imagen
├── requirements.txt      # librerías que usa la inferencia, con versión
├── inferencia.py         # carga el modelo y predice
├── modelo.joblib         # imputador, escaladores, coordenadas, red y umbral, guardados desde el notebook
├── ejecutar.sh           # arma la imagen y corre el contenedor
├── lluvia_ejemplo.csv    # 20 días de test para probar
├── .gitattributes        # mantiene ejecutar.sh con saltos de línea de Linux
└── README.md
```

## Entrada y salida

- **Entrada:** un CSV con las columnas originales del dataset (`Date`, `Location`, `MinTemp`, `MaxTemp`, `Rainfall`, `Evaporation`, `Sunshine`, `WindGustDir`, `WindGustSpeed`, `WindDir9am`, `WindDir3pm`, `WindSpeed9am`, `WindSpeed3pm`, `Humidity9am`, `Humidity3pm`, `Pressure9am`, `Pressure3pm`, `Cloud9am`, `Cloud3pm`, `Temp9am`, `Temp3pm`, `RainToday`). Puede tener faltantes, el script los completa igual que el notebook. Las columnas de más se ignoran. Si falta alguna columna o aparece una ciudad que no está en el dataset, el script avisa y no predice.
- **Salida:** el mismo CSV con dos columnas nuevas, `prob_lluvia` (probabilidad de que llueva mañana) y `llueve_manana` (`Yes` si la probabilidad supera el umbral elegido en validación, `No` si no).

El script no ajusta nada con los datos nuevos. Todo lo aprendido en train (imputador, escaladores, red y umbral) viene en `modelo.joblib`.

## Cómo ejecutarlo

Hace falta tener Docker instalado y abierto. Los comandos se ejecutan desde esta carpeta (`docker/`), con una terminal de bash (en Linux o macOS la terminal normal, en Windows Git Bash).

Con el script, que arma la imagen y corre el contenedor en un solo paso (el CSV de entrada tiene que estar en esta carpeta, y el de salida queda acá):

```bash
./ejecutar.sh lluvia_ejemplo.csv predicciones.csv
```

Si el sistema no deja ejecutarlo, primero hay que darle permiso con `chmod +x ejecutar.sh`, o correrlo con `bash ejecutar.sh lluvia_ejemplo.csv predicciones.csv`.

El script hace estos dos pasos, que también se pueden correr a mano:

1. Armar la imagen:

```bash
docker build -t prediccion-lluvia .
```

2. Correr el contenedor. La carpeta actual se monta como `/datos` dentro del contenedor, así el script lee el CSV de entrada y escribe el de salida acá:

```bash
docker run --rm -v "$(pwd)":/datos prediccion-lluvia /datos/lluvia_ejemplo.csv /datos/predicciones.csv
```

Al terminar queda `predicciones.csv` en esta carpeta. Para predecir otros días se reemplaza `lluvia_ejemplo.csv` por otro archivo con las mismas columnas.
