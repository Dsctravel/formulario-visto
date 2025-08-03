import streamlit as st

# Etapa de Location Information (Consulado)
def exibir():
    st.subheader("Location Information")
    opcoes = ["", "São Paulo", "Rio de Janeiro", "Recife", "Brasília", "Porto Alegre"]
    default_index = st.session_state.get("consulado_index", 0)
    escolha = st.selectbox(
        "Local onde você irá submeter sua solicitação:",
        options=opcoes,
        index=default_index,
        key="consulado_index"
    )
    # Opcional: mostrar confirmação
    if escolha:
        st.write(f"Consulado selecionado: {escolha}")
