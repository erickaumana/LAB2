import pandas as pd
import numpy as np

#Cargar archivo CSV
df = pd.read_csv("Datos_Lab2.csv", encoding="latin1")

#Realizar calculos
df["TR min/u total"] = df["TR min/u"] * df["Qty"]
df["Tci min/kilo"] = df["TR min/u total"] * df["%U"] * (1/(2-df["Er"])) * (1/df["Vi"])
df ["Tc/TktT"] = df["Tci min/kilo"] / df["Takt Time Meta min/U"]
df["No MQ"] = np.ceil(df["Tc/TktT"])
df["Takt Time Prod. Min/Un"] = df["Tci min/kilo"] / df["No MQ"]
df["Minutos disponibles por mes-turno"] = 4 * 5 * df["Horas Disponibles por Turno"] * 60
df["Minutos totales de carga"] = df["Takt Time Prod. Min/Un"] * df["Qty"]



resta_necesaria = df["Minutos disponibles por mes-turno"] - df["Minutos totales de carga"]

#0 si resta es igual o mayor; operacion si es menor que 0.
df["HORAS EXTRA"] = np.where(
    resta_necesaria >= 0,
    0,
    -1 * resta_necesaria / 60
)

#Crear csv final
df.to_csv("resultado.csv", index=False)




