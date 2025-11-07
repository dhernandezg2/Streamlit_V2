import streamlit as st

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
else:
    st.sidebar.button("Cargar")

st.sidebar.divider()

# ============ FILTROS (UI sin lógica) ============
st.sidebar.header("Filtros")
tipos_vehiculo = st.sidebar.multiselect("Tipo de vehículo", ["Turismo", "Camión", "Ambulancia"])  #tipos de vehiculo
tipos_combustible = st.sidebar.multiselect("Tipo de combustible", ["Gasolina", "Gasoil", "Gas"])  #tipos de combustible
lugar = st.sidebar.text_input("Dirección")
