
import pandas as pd

#Filtra el dataframe segun el tipo de vehiculo
def filtro_tipo_vehiculo(df, tipos_vehiculo):

    if df is None:
        return None
    
    #Si no se selecciona ningun vehículo
    if not tipos_vehiculo:
        return df
    
    return df[df["tipo_vehiculo"].isin(tipos_vehiculo)]

#Filtra el dataframe segun el tipo de combustible
def filtro_tipo_combustible(df,tipos_combustible):

    if df is None:
        return None
    
    #Si no se selecciona ningun combustible
    if not tipos_combustible:
        return df
    
    return df[df["tipo_combustible"].isin(tipos_combustible)]

#Filtra el dataframe segun la direccion
def filtro_direccion(df, lugar):

    if df is None:
        return None
    
    #Si no se selecciona ninguna direccion
    if not lugar:
        return df
    
    return df[df["direccion"].astype(str).str.contains(str(lugar), case = False, na = False)]


#Filtros juntos
def aplicar_filtros(df,tipos_vehiculo,tipos_combustible,lugar):
    
    if df is None:
        return None
     
    df_filtrado = df.copy()

    #Filtramos por vehiculo
    if tipos_vehiculo:
         df_filtrado = filtro_tipo_vehiculo(df_filtrado, tipos_vehiculo)

    #Filtramos por combustible
    if tipos_combustible:
         df_filtrado = filtro_tipo_combustible(df_filtrado, tipos_combustible)

    #Filtramos por direccion
    if lugar:
         df_filtrado = filtro_tipo_combustible(df_filtrado, lugar)

    return df_filtrado