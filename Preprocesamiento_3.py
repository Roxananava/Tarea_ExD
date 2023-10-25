"""Navarrete Anguiano Roxana Aurora
Grupo 501
24 de Octubre 2023"""

"""Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y 
otro parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados."""

import pandas as pd

def min_max(data, columnas):
    for columna in columnas:
        max_columna = data[columna].max()

        data[f"escalasoSim_{data[columna].name}"] = data[columna] / max_columna
    return print(data)

#DATOS DE PRUEBA
personas= {"salario": [20000, 10000, 40000, 25000, 60000],
            "edad": [20, 18, 35, 40, 45]}
data = pd.DataFrame(personas)

min_max(data, ["edad"])

