import streamlit as st
import pandas as pd

#Funciones externas
from modulos.filtros import aplicar_filtros


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
tipos_vehiculo = st.sidebar.multiselect("Tipo de vehículo", ["Furgoneta", "Camión", "Sedán"])  #tipos de vehículo
tipos_combustible = st.sidebar.multiselect("Tipo de combustible", ["Gasolina", "Gasoil", "Gas"])  #tipos de combustible
lugar = st.sidebar.text_input("Dirección") #Direccion

parametro = st.sidebar.selectbox("Parámetro", ["Repostado", "Distancia", "Consumo"])
rango_valores = st.sidebar.slider("Rango de valores", 0, 100, (10, 90))
rango_fechas = st.sidebar.date_input("Rango de fechas", [])

aplicar = st.sidebar.button("Aplicar filtros")

#Hacemos que los rangos sean dinamicos y no sean siempre 0 - 100
if df is not None and parametro.lower() in df.columns:
    min_val = float(df[parametro.lower()].min())
    max_val = float(df[parametro.lower()].max())
else:
    min_val, max_val = 0, 100

rango_valores = st.sidebar.slider("Rango de valores", min_val, max_val, (min_val, max_val))


if aplicar:

    #Aplicamos los filtros de la columna de la izquierda.
    if df is not None:

        lugar = (lugar or "").strip() or None

        df_filtrado = aplicar_filtros(
            df,
            tipos_vehiculo = tipos_vehiculo,
            tipos_combustible = tipos_combustible,
            lugar = lugar,
            parametro = parametro,
            rango = rango_valores
            )

        st.subheader(f"Resultados filtrados ({len(df_filtrado)} filas)")
        st.dataframe(df_filtrado, use_container_width = True)

# CONTENIDO PRINCIPAL 
st.divider()
st.subheader("📊 Vehículos agrupados por número de repostajes")

st.write("")

st.subheader("📈 Gráficos de análisis")

st.divider()
st.subheader("🔎 Detalle por matrícula")