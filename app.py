import streamlit as st
import pandas as pd

#Funciones externas
from modulos.filtros import filtrar_por_tipo_vehiculo


# CONFIGURACIÓN GENERAL 
st.set_page_config(page_title="Repostajes", layout="wide")
st.title("🚗 Análisis de Repostajes")

# CARGA DE DATOS
st.sidebar.header("Datos de entrada")
modo = st.sidebar.radio("Fuente de datos", ["📤 Subir archivo"])

if modo == "📤 Subir archivo":
    archivo = st.sidebar.file_uploader("Sube un Excel (.xlsx)", type=["xlsx"])
    if archivo:

        df = pd.read_excel(archivo)  #lee el excel que se carga

        #Vista previa de los datos subidos
        st.subheader("Vista previa de los datos")
        st.dataframe(df.head(10), use_container_width = True) 

        #Transformo las columnas a minusculas
        df.columns = df.columns.str.lower().str.strip()
    
    else:
        df = None
else:
    st.sidebar.button("Cargar")

st.sidebar.divider()

# FILTROS LATERALES
st.sidebar.header("Filtros")
tipos_vehiculo = st.sidebar.multiselect("Tipo de vehículo", ["Turismo", "Camión", "Ambulancia"])  #tipos de vehículo
tipos_combustible = st.sidebar.multiselect("Tipo de combustible", ["Gasolina", "Gasoil", "Gas"])  #tipos de combustible
lugar = st.sidebar.text_input("Dirección")

parametro = st.sidebar.selectbox("Parámetro", ["Repostado", "Distancia", "Consumo"])
rango_valores = st.sidebar.slider("Rango de valores", 0, 100, (10, 90))
rango_fechas = st.sidebar.date_input("Rango de fechas", [])

aplicar = st.sidebar.button("Aplicar filtros")

if aplicar:

    #Aplicamos el filtro de vehículo.
    if df is not None:
        df_filtrado = filtrar_por_tipo_vehiculo(df,tipos_vehiculo)

        st.subheader(f"Resultados filtrados ({len(df_filtrado)} filas)")
        st.dataframe(df_filtrado, use_container_width = True)

# CONTENIDO PRINCIPAL 
st.divider()
st.subheader("📊 Vehículos agrupados por número de repostajes")

st.write("")

st.subheader("📈 Gráficos de análisis")

st.divider()
st.subheader("🔎 Detalle por matrícula")