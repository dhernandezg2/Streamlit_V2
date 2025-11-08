
import pandas as pd

#Filtra el dataframe segun el tipo de vehiculo
def filtro_tipo_vehiculo(df, tipos_vehiculo):

    if df is None:
        return None
    
    #Si no se selecciona ningun vehículo
    if not tipos_vehiculo:
        return df
    
    return df[df["tipo_vehiculo"].isin(tipos_vehiculo)]
