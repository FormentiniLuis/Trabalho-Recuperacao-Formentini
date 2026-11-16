import streamlit as st

st.set_page_config(
    page_title="Escolas Prioritárias",
    layout="wide"
)
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    st.image("images/logo_sedu.png", width=420)
st.title("Escolas Prioritárias")

st.subheader(
    "Análise e acompanhamento de indicadores educacionais"
)

col1, col2 = st.columns(
    [4, 1],
    vertical_alignment="center"
)

with col1:
    st.write("Trabalho de Recuperação")
    st.markdown(
    "<p style='font-size:22px;'>Autor: Luís Formentini</p>",
    unsafe_allow_html=True
)

with col2:
    st.image("images/foto_autor.jpg", width=240)

st.divider()
st.sidebar.image("images/brasao_es.png", width=180)
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
if secao == "Apresentação":
    st.header("Apresentação")
    st.write(
        "Bem-vindo ao aplicativo Escolas Prioritárias. "
        "Este espaço será destinado ao acompanhamento "
        "de indicadores educacionais."
    )

elif secao == "Escolas Prioritárias":
    st.header("Escolas Prioritárias")
    st.info("Espaço reservado para as listas de 2025 e 2026.")

elif secao == "Indicadores Educacionais":
    st.header("Indicadores Educacionais")
    st.info("Espaço reservado para os indicadores educacionais.")

elif secao == "Resultados de Aprendizagem":
    st.header("Resultados de Aprendizagem")
    st.info("Espaço reservado para os resultados do PAEBES e AMA.")

elif secao == "Fluxo Escolar":
    st.header("Fluxo Escolar")
    st.info("Espaço reservado para aprovação, reprovação e abandono.")

elif secao == "Série Histórica":
    st.header("Série Histórica")
    st.info("Espaço reservado para a evolução dos indicadores.")

elif secao == "Distribuição Geográfica":
    st.header("Distribuição Geográfica")
    st.info("Espaço reservado para o mapa das Escolas Prioritárias.")

elif secao == "Análises e Comparações":
    st.header("Análises e Comparações")
    st.info("Espaço reservado para análises comparativas.")
