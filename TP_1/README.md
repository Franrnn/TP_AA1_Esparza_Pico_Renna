# TP Regresión — Aprendizaje Automático 1

Trabajo práctico de la materia **Aprendizaje Automático 1** de la Tecnicatura Universitaria en Inteligencia Artificial (FCEIA - UNR).

**Objetivo:** predecir el valor mediano de las viviendas de cada barrio de Boston (`MEDV`, en miles de dólares) a partir de 13 características del barrio, usando regresión lineal múltiple, descenso del gradiente y modelos regularizados (Ridge, Lasso, ElasticNet).

## Integrantes

- Franco Esparza
- Franco Renna
- Leandro Picó

## Estructura del repositorio

| Archivo / carpeta | Contenido |
|---|---|
| `TP-regresion-AA1.ipynb` | **Notebook del TP.** Es el informe: análisis exploratorio, preprocesamiento, modelos y conclusiones |
| `house-prices-tp.csv` | Dataset (556 filas, 14 columnas) |
| `requirements.txt` | Librerías necesarias |

## Cómo ejecutarlo

```powershell
py -3.14 -m venv .entorno-aa1
.\.entorno-aa1\Scripts\python.exe -m pip install -r requirements.txt
```

Después se abre `TP-regresion-AA1.ipynb` en VS Code o Jupyter, se elige el kernel `.entorno-aa1` y se ejecutan todas las celdas.
