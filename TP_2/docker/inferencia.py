# Predicción de lluvia para el día siguiente con el modelo entrenado en el notebook
# Uso: python inferencia.py entrada.csv salida.csv
import os
import sys
# Para que TensorFlow no llene la salida con avisos al cargar la red
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# TensorFlow se importa antes que scikit-learn, porque en Windows al revés falla al cargar sus librerías
import tensorflow as tf
import joblib
import numpy as np
import pandas as pd

# Busca el modelo en la misma carpeta que este script
RUTA_MODELO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modelo.joblib')


def cargar_modelo(ruta=RUTA_MODELO):
    # El archivo tiene todo lo aprendido en train: imputador, modas del viento, coordenadas, escaladores, red y umbral
    return joblib.load(ruta)


def preparar(datos, art):
    # Repite el preprocesamiento del notebook sin ajustar nada, solo usa lo guardado
    numericas = list(art['escala_knn'].feature_names_in_)
    viento = list(art['moda_ciudad'].columns)
    faltan = [c for c in ['Date', 'Location'] + numericas + viento if c not in datos.columns]
    if faltan:
        raise ValueError(f'Faltan columnas en el CSV de entrada: {faltan}')

    datos = datos.copy()
    datos['Date'] = pd.to_datetime(datos['Date'])
    ciudades_nuevas = set(datos['Location']) - set(art['coordenadas'].index)
    if ciudades_nuevas:
        raise ValueError(f'Ciudades sin coordenadas, el modelo no las conoce: {ciudades_nuevas}')

    # Nubosidad 9 no es un valor posible
    for col in ['Cloud9am', 'Cloud3pm']:
        datos.loc[datos[col] > 8, col] = np.nan

    # Imputación con KNN, escalando solo para medir distancias
    escala = art['escala_knn']
    imputado = art['imputador_knn'].transform(escala.transform(datos[numericas]))
    datos[numericas] = escala.inverse_transform(imputado)

    # Ajustes después de imputar
    datos[['Cloud9am', 'Cloud3pm']] = datos[['Cloud9am', 'Cloud3pm']].round().clip(0, 8)
    datos['RainToday'] = (datos['Rainfall'] > 1).astype(int)
    for col in viento:
        datos[col] = datos[col].fillna(datos['Location'].map(art['moda_ciudad'][col])).fillna(art['moda_general'][col])

    # Ciudad como coordenadas, mes y viento como ángulos
    datos['Lat'] = datos['Location'].map(art['coordenadas']['Lat'])
    datos['Lon'] = datos['Location'].map(art['coordenadas']['Lon'])
    mes = datos['Date'].dt.month
    datos['Mes_sin'] = np.sin(2 * np.pi * mes / 12)
    datos['Mes_cos'] = np.cos(2 * np.pi * mes / 12)
    for col in viento:
        angulo = 2 * np.pi * datos[col].map(art['orden_viento']) / 16
        datos[col + '_sin'] = np.sin(angulo)
        datos[col + '_cos'] = np.cos(angulo)

    # Escalado y columnas en el mismo orden que en el entrenamiento
    escalador = art['escalador']
    a_escalar = list(escalador.feature_names_in_)
    datos[a_escalar] = escalador.transform(datos[a_escalar])
    return datos[art['columnas']]


def predecir(datos, art):
    X = preparar(datos, art)
    # La red devuelve la probabilidad de lluvia de cada día
    prob = art['modelo'].predict(X, verbose=0).ravel()
    return prob, np.where(prob >= art['umbral'], 'Yes', 'No')


def main():
    if len(sys.argv) != 3:
        print('Uso: python inferencia.py entrada.csv salida.csv')
        sys.exit(1)
    entrada, salida = sys.argv[1], sys.argv[2]

    art = cargar_modelo()
    datos = pd.read_csv(entrada)
    prob, clase = predecir(datos, art)

    resultado = datos.copy()
    resultado['prob_lluvia'] = prob.round(4)
    resultado['llueve_manana'] = clase
    resultado.to_csv(salida, index=False)
    print(f'{len(resultado)} predicciones guardadas en {salida}')


if __name__ == '__main__':
    main()
