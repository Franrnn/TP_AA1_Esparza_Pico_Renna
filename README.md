# Aprendizaje Automático 1 — Regresión y clasificación

Trabajos prácticos de la materia **Aprendizaje Automático 1** de la Tecnicatura Universitaria en Inteligencia Artificial (FCEIA, UNR).

**Equipo:** Franco Esparza · Leandro Picó · Franco Renna

## Proyectos

| Proyecto | Problema | Técnicas | Estado |
|---|---|---|---|
| [**Regresión: precio de viviendas**](TP_1/) | Predecir el valor mediano de las viviendas de cada barrio a partir de 13 características | Regresión lineal múltiple, descenso del gradiente, Ridge, Lasso, ElasticNet, validación cruzada | Entregado. ElasticNet explica cerca del 70% de la variación del precio en datos nuevos (R² 0,68 en test) |
| [**Clasificación: lluvia en Australia**](TP_2/) | Predecir a las 23:59 si al día siguiente va a llover en 49 ciudades (145.000 registros meteorológicos) | Limpieza de datos, imputación con KNN, regresión logística, comparación de modelos | En curso |

Cada carpeta tiene su propio README con el detalle y las instrucciones para ejecutarlo. El desarrollo completo, con el análisis exploratorio y las conclusiones, está en el notebook de cada trabajo.

## Stack

Python · Pandas · NumPy · scikit-learn · Matplotlib · Seaborn · PyCaret (TP2)

## Estructura

```
├── TP_1/   regresión: notebook, dataset y requirements.txt
└── TP_2/   clasificación: notebook, dataset y requirements.txt
```
