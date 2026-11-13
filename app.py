import streamlit as st

st.set_page_config(
    page_title="Escolas Prioritárias",
    layout="wide"
)
st.title("Escolas Prioritárias")

st.subheader(
    "Análise e acompanhamento de indicadores educacionais"
)

st.write("Trabalho de Recuperação")
st.write("Autor: Luís Formentini")

st.divider()
st.sidebar.title("Navegação")

secao = st.sidebar.radio(
    "Selecione uma seção:",
    [
        "Apresentação",
        "Escolas Prioritárias",
        "Indicadores Educacionais",
        "Resultados de Aprendizagem",
        "Fluxo Escolar",
        "Série Histórica",
        "Distribuição Geográfica",
        "Análises e Comparações"
    ]
)
