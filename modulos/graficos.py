import plotly.express as px

#Histogramas para los diferentes parametros
def Grafico_lineal_parametros(df,parametro):

    if df is None or df.empty:
        return None
    
    columna = parametro.lower()

    if columna not in df.columns:
        return None
    
    #Filtramos por fecha para ordenarlas
    if "fecha" in df.columns:
        df = df.sort_values("fecha")
        eje_x = "fecha"
    
    #Creamos el grafico lineal
    fig = px.line(
        df,
        x = eje_x,
        y = columna,
        markers= True,
        title = f"Evolución de {columna}",
        color_discrete_sequence = ["#1f77b4"]
    )

    fig.update_traces(line = dict(width=2))
    fig.update_layout(
        xaxis_title = "fecha" if eje_x == "fecha" else "",
        yaxis_title = columna,
        template = "plotly_white",
    )

    return fig