import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  

st.set_page_config(
    page_title='PROYECTOS IZZI',
    page_icon='🛰️',  
)

st.title("PROYECTOS IZZI")

tabs = st.tabs(
    ["CONFIGURACIONES", "LICENCIAS UTILIZADAS", "TENDENCIA LICENCIAS"]
)

with tabs[0]:
    df_config = pd.DataFrame([
        {"Proyecto": "Staff online", "Downstream": 16, "Upstream": 12}
    ])
    st.dataframe(df_config)
    ax = df_config.set_index("Proyecto")[["Downstream", "Upstream"]].plot(kind="bar")
    plt.ylabel("Cantidad")
    plt.title("")
    st.pyplot(plt.gcf())
    plt.clf()

with tabs[1]:
    df_lic = pd.DataFrame([
        {"Tipo": "Gen1", "Downstream": 1041, "Upstream": 87},
        {"Tipo": "Gen2", "Downstream": 549, "Upstream": 172},
        {"Tipo": "Integracion", "Downstream": 24692, "Upstream": 6575},
        {"Tipo": "Docsis 3.1", "Downstream": 5427, "Upstream": None}
    ])
    st.dataframe(df_lic)
    ax2 = df_lic.set_index("Tipo")[["Downstream", "Upstream"]].plot(kind="bar")
    plt.ylabel("Cantidad")
    plt.title("")
    st.pyplot(plt.gcf())
    plt.clf()

with tabs[2]:
    st.write("Tendencia de licencias (por implementar)")
