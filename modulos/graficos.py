import plotly.express as px

#Histogramas para los diferentes parametros
def histogramas_parametros(df,parametro):

    if df is None or df.empty:
        return None
    
    columna = parametro.lower()

    if columna not in df.columns:
        return None
    
    #Creamos el histograma
    fig = px.histogram(
        df,
        x = columna,
        nbins = 15,
        title = f"Distribucion de {columna}",
        color_discrete_sequence = ["#1f77b4"]
    )

    fig.update_layout(
        xaxis_title = columna,
        yaxis_title = "frecuencia",
        template = "plotly_white",
        bargap = 0.1
    )

    return fig