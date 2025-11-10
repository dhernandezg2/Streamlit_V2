import streamlit as st
import pandas as pd

if "df_filtrado" not in st.session_state:
    st.session_state.df_filtrado = None

#Funciones externas
from modulos.filtros import aplicar_filtros
from modulos.graficos import histogramas_parametros


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
rango_fechas = st.sidebar.date_input("Rango de fechas", [])

aplicar = st.sidebar.button("Aplicar filtros")

#Hacemos que los rangos sean dinamicos y no sean siempre 0 - 100 (para los valores numericos)
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
        st.session_state.df_filtrado = df_filtrado

        st.subheader(f"Resultados filtrados ({len(df_filtrado)} filas)")
        st.dataframe(df_filtrado, use_container_width = True)

    
    # SELECCION DEL VEHICULO

    st.divider()
    st.subheader("Analisis individual del vehiculo")

    df_filtrado = st.session_state.df_filtrado

    if df is None:

        st.info("Sube el archivo")

    else:

        if "vehiculo" not in df.columns:

            st.warning("No existe columna de vehiculos")

        elif df_filtrado is None or df_filtrado.empty:

            st.info("No hay informacion en el datashet")

        else:

            vehiculos = (df_filtrado["vehiculo"].astype(str).dropna().unique())

            vehiculos = sorted([vehiculo for vehiculo in vehiculos if vehiculo.strip() != ""])

            if len(vehiculos) == 0:

                st.info("No hay vehiculos")

            else:

                vehiculo_seleccionado = st.selectbox("Selecciona la matricula", vehiculos, index = 0)

                df_vehiculo = df_filtrado[df_filtrado["vehiculo"].astype(str) == str(vehiculo_seleccionado)]

                st.dataframe(df_vehiculo, use_container_width = True)

    #Histogramas del vehiculo
    st.divider()
    st.subheader(f"histograma de {parametro} del vehiculo seleccionado")

    fig = histogramas_parametros(df_vehiculo, parametro)

    if fig:
        st.plotly_chart(fig, use_container_width = True)
    else:
        st.warning("No se generó el histograma")

# CONTENIDO PRINCIPAL 
st.divider()
st.subheader("📊 Vehículos agrupados por número de repostajes")

st.write("")

st.subheader("📈 Gráficos de análisis")