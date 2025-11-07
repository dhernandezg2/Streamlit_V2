import streamlit as st

# ============ CONFIGURACIÓN GENERAL ============
st.set_page_config(page_title="Repostajes", layout="wide")
st.title("🚗 Análisis de Repostajes")
st.caption("Prototipo")

# ============ CARGA (UI sin lógica) ============
st.sidebar.header("Datos de entrada")
modo = st.sidebar.radio("Fuente de datos", ["📤 Subir archivo", "📁 Ruta local"])

if modo == "📤 Subir archivo":
    archivo = st.sidebar.file_uploader("Sube un Excel (.xlsx)", type=["xlsx"])
    if archivo:
        st.success("Archivo cargado")
else:
    ruta = st.sidebar.text_input("Ruta del Excel", "Ruta/Repostajes.xlsx")
    st.sidebar.button("Cargar")

st.sidebar.divider()







