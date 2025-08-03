import streamlit as st
from pages.informacoes_pessoais_1 import formulario_pessoal

st.set_page_config(layout="wide")
st.title("Formulário de Visto")

with st.sidebar:
    aba = st.radio("Etapas", ["Informações Pessoais 1"])

if aba == "Informações Pessoais 1":
    formulario_pessoal()
