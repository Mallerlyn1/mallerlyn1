!pip install plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard IZZI", page_icon="📊", layout="wide")
st.title("📊 Dashboard Licenciamiento")

# Datos manuales
df_config = pd.DataFrame([
    {"Proyecto": "Staff online", "Downstream": 16, "Upstream": 12}
])

df_licencias = pd.DataFrame([
    {"Tipo": "GEN1", "DS": 100, "US": 80},
    {"Tipo": "GEN2", "DS": 340, "US": 160},
    {"Tipo": "INTEGRACION", "DS": 24692, "US": 6575},
    {"Tipo": "DOCSIS 3.1", "DS": 5427, "US": None},
    {"Tipo": "STAFF", "Aplicadas_DS": 10, "Aplicadas_US": 23}
])

# Crear pestañas
tabs = st.tabs(["CONFIGURACIONES", "LICENCIAS UTILIZADAS", "TENDENCIA LICENCIAS"])

# CONFIGURACIONES
with tabs[0]:
    st.subheader("⚙️ Configuraciones del Proyecto")
    st.dataframe(df_config)

# LICENCIAS UTILIZADAS
with tabs[1]:
    st.subheader("📋 Licencias Utilizadas")
    df_utilizadas = df_licencias.dropna(subset=["DS", "US"], how="all")
    st.dataframe(df_utilizadas[["Tipo", "DS", "US"]].rename(columns={"DS": "Downstream", "US": "Upstream"}))

    fig_ds_us = px.bar(df_utilizadas, x="Tipo", y=["DS", "US"], barmode="group", title="Licencias por Canal (DS y US)")
    st.plotly_chart(fig_ds_us, use_container_width=True)

# TENDENCIA LICENCIAS
with tabs[2]:
    st.subheader("📈 Tendencia de Licencias")
    df_aplicadas = df_licencias[["Tipo", "Aplicadas_DS", "Aplicadas_US"]].dropna(how="all", subset=["Aplicadas_DS", "Aplicadas_US"])
    if not df_aplicadas.empty:
        fig_aplicadas = px.bar(df_aplicadas, x="Tipo", y=["Aplicadas_DS", "Aplicadas_US"], barmode="group", title="Licencias Aplicadas (STAFF)")
        st.plotly_chart(fig_aplicadas, use_container_width=True)
    else:
        st.info("No hay datos de licencias aplicadas para mostrar.")
