#!/bin/bash
# Arma la imagen de Docker y predice si mañana llueve para los días de un CSV
# Uso, con los CSV en esta carpeta: ./ejecutar.sh entrada.csv salida.csv
set -e

if [ "$#" -ne 2 ]; then
    echo "Uso: ./ejecutar.sh entrada.csv salida.csv"
    exit 1
fi

# Trabaja siempre en la carpeta del script, donde están el Dockerfile y los CSV
cd "$(dirname "$0")"

# En Git Bash (Windows) hace falta la ruta con letra de unidad y evitar que cambie las rutas /datos/...
# En Linux y macOS pwd -W no existe y se usa pwd normal
CARPETA="$(pwd -W 2>/dev/null || pwd)"
export MSYS_NO_PATHCONV=1

docker build -t prediccion-lluvia .
docker run --rm -v "$CARPETA":/datos prediccion-lluvia "/datos/$1" "/datos/$2"
