import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import pandas as pd

# Título de la sección
st.title("Comparación del pH Isoeléctrico (pI) de la Histidina y otras Moléculas")

# Datos de ejemplo: pH isoeléctrico (pI) de diferentes moléculas
datos = {
    "Molécula": ["Histidina", "Albumina", "Hemoglobina", "Mioglobina", "Caseína"],
    "pI": [7.59, 4.9, 6.8, 7.0, 4.6]
}

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Crear la gráfica usando Plotly Express
fig = px.bar(
    df,
    x="Molécula",
    y="pI",
    text="pI",
    title="pH Isoeléctrico (pI) de la Histidina y otras Moléculas",
    labels={"pI": "pH Isoeléctrico", "Molécula": "Moléculas"},
    color="Molécula",
    color_discrete_sequence=px.colors.qualitative.Set2
)

# Configurar la apariencia de la gráfica
fig.update_traces(textposition="outside")
fig.update_layout(
    template="plotly_white",
    yaxis=dict(range=[0, 8], title="pH Isoeléctrico"),
    xaxis_title="Moléculas",
    title_x=0.5
)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig)

