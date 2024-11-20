import streamlit as st
import pandas as pd
import plotly.express as px
import py3Dmol

# Configuración inicial de la página
st.set_page_config(page_title="Dashboard de Histidina", layout="wide")

# Título del dashboard
st.title("Dashboard Interactivo: Histidina")

# Descripción general
st.markdown("""
La **histidina** es un aminoácido esencial involucrado en múltiples procesos biológicos. Este dashboard interactivo te permitirá explorar:
- Información general.
- Comparación del pH isoeléctrico con otras moléculas.
- Visualización interactiva de su estructura 3D.
""")

# Sidebar con opciones
st.sidebar.title("Opciones")
mostrar_info = st.sidebar.checkbox("Mostrar información general", value=True)
mostrar_grafica = st.sidebar.checkbox("Mostrar gráfica comparativa", value=True)
mostrar_modelo = st.sidebar.checkbox("Mostrar modelo 3D", value=True)

# Función para renderizar el modelo 3D de la histidina
def render_modelo_3d():
    histidina_pdb = """
HETATM    1  N   HIS A   1      -1.204   0.689   0.000  1.00  0.00           N  
HETATM    2  CA  HIS A   1      -0.012   0.000   0.000  1.00  0.00           C  
HETATM    3  C   HIS A   1       1.264   0.763   0.000  1.00  0.00           C  
HETATM    4  O   HIS A   1       1.304   2.000   0.000  1.00  0.00           O  
HETATM    5  CB  HIS A   1      -0.312  -1.523   0.000  1.00  0.00           C  
HETATM    6  CG  HIS A   1      -0.890  -2.089   1.222  1.00  0.00           C  
HETATM    7  ND1 HIS A   1      -1.812  -1.241   2.035  1.00  0.00           N  
HETATM    8  CD2 HIS A   1      -0.768  -3.366   1.799  1.00  0.00           C  
HETATM    9  CE1 HIS A   1      -2.209  -1.921   3.126  1.00  0.00           C  
HETATM   10  NE2 HIS A   1      -1.516  -3.110   2.963  1.00  0.00           N  
HETATM   11  H   HIS A   1      -1.204   1.677   0.000  1.00  0.00           H  
HETATM   12  HA  HIS A   1      -0.001  -0.024   0.987  1.00  0.00           H  
HETATM   13  HB2 HIS A   1       0.012  -1.877   0.000  1.00  0.00           H  
HETATM   14  HB3 HIS A   1      -0.898  -1.853  -0.863  1.00  0.00           H  
"""
    viewer = py3Dmol.view(width=800, height=400)
    viewer.addModel(histidina_pdb, 'pdb')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    return viewer

# Información general
if mostrar_info:
    st.subheader("Información General")
    st.markdown("""
    - **Fórmula molecular**: C₆H₉N₃O₂  
    - **Masa molecular**: 155.15 g/mol  
    - **pH isoeléctrico (pI)**: 7.59  
    - **Clasificación**: Aminoácido esencial.  
    - **Funciones**:
        - Precursor de histamina.
        - Participa en la regulación del pH.
        - Componente clave en sitios activos de enzimas.  
    """)

# Gráfica comparativa
if mostrar_grafica:
    st.subheader("Comparación del pH Isoeléctrico (pI)")
    datos = {
        "Molécula": ["Histidina", "Albumina", "Hemoglobina", "Mioglobina", "Caseína"],
        "pI": [7.59, 4.9, 6.8, 7.0, 4.6]
    }
    df = pd.DataFrame(datos)

    fig = px.bar(
        df,
        x="Molécula",
        y="pI",
        text="pI",
        title="pH Isoeléctrico de la Histidina comparado con otras moléculas",
        labels={"pI": "pH Isoeléctrico", "Molécula": "Moléculas"},
        color="Molécula",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(template="plotly_white", title_x=0.5)

    st.plotly_chart(fig)

# Modelo 3D
if mostrar_modelo:
    st.subheader("Modelo 3D de la Histidina")
    modelo_3d = render_modelo_3d()
    modelo_html = modelo_3d._make_html()
    st.components.v1.html(modelo_html, width=800, height=400)
