# test_adicional.py

import streamlit as st
from steps.informacoes_trabalho_educacao_adicional import exibir

st.set_page_config(
    page_title="🧪 Teste Aba: Additional Work/Education/Training",
    layout="wide"
)

st.title("🧪 Teste da Aba: Additional Work/Education/Training Information")
exibir()
