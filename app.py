import streamlit as st
import pandas as pd

# ============ CONFIGURACIÓN GENERAL ============
st.set_page_config(page_title="Repostajes", layout="wide")
st.title("🚗 Análisis de Repostajes")

# ============ CARGA (UI sin lógica) ============
st.sidebar.header("Datos de entrada")
modo = st.sidebar.radio("Fuente de datos", ["📤 Subir archivo"])

if modo == "📤 Subir archivo":
    archivo = st.sidebar.file_uploader("Sube un Excel (.xlsx)", type=["xlsx"])
    if archivo:
        st.success("Archivo cargado")

        df = pd.read_excel(archivo)  #lee el excel que se carga

        #Vista previa de los datos subidos
        st.subheader("Vista previa de los datos")
        st.dataframe(df.head(10), use_container_width = True) 
    
    else:
        df = None
else:
    st.sidebar.button("Cargar")

st.sidebar.divider()

# ============ FILTROS (UI sin lógica) ============
st.sidebar.header("Filtros")
tipos_vehiculo = st.sidebar.multiselect("Tipo de vehículo", ["Turismo", "Camión", "Ambulancia"])  #tipos de vehiculo
tipos_combustible = st.sidebar.multiselect("Tipo de combustible", ["Gasolina", "Gasoil", "Gas"])  #tipos de combustible
lugar = st.sidebar.text_input("Dirección")

parametro = st.sidebar.selectbox("Parámetro", ["Repostado", "Distancia", "Consumo"])
rango_valores = st.sidebar.slider("Rango de valores", 0, 100, (10, 90))
rango_fechas = st.sidebar.date_input("Rango de fechas", [])

aplicar = st.sidebar.button("Aplicar filtros")

# ============ CONTENIDO PRINCIPAL ============
st.divider()
st.subheader("📊 Vehículos agrupados por número de repostajes")

st.write("")

st.subheader("📈 Gráficos de análisis")

st.divider()
st.subheader("🔎 Detalle por matrícula")