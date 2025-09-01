import streamlit as st
import pandas as pd
 

st.set_page_config(
    page_title='PROYECTOS IZZI',
    page_icon='🛰️',  
)

st.title("PROYECTOS IZZI")

tabs = st.tabs(
    ["CONFIGURACIONES", "LICENCIAS UTILIZADAS", "TENDENCIA LICENCIAS"]
)

with tabs[0]:
     st.dataFrame([
        {"Proyecto": "Staff online", "Downstream": 16, "Upstream": 12}
    ])
   

with tabs[1]:
     st.dataFrame([
        {"Tipo": "Gen1", "Downstream": 1041, "Upstream": 87},
        {"Tipo": "Gen2", "Downstream": 549, "Upstream": 172},
        {"Tipo": "Integracion", "Downstream": 24692, "Upstream": 6575},
        {"Tipo": "Docsis 3.1", "Downstream": 5427, "Upstream": None}
    ])
   
with tabs[2]:
    st.write("Tendencia de licencias (por implementar)")
