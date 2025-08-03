import streamlit as st

def exibir():
    st.subheader("Segurança e Antecedentes - Parte 4")

    # 1) Fraude ou falsa declaração para obtenção de visto/imigração
    fraude = st.radio(
        "Você já tentou obter ou ajudou outros a obter visto, entrada nos EUA ou outro benefício de imigração dos EUA por fraude, falsa declaração intencional ou outros meios ilegais?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="fraude_visto"
    )
    if st.session_state.fraude_visto == "Sim":
        st.text_area(
            "Se sim, descreva:",
            key="detalhes_fraude",
            height=100
        )

    # 2) Remoção ou deportação de algum país
    deportado = st.radio(
        "Você já foi removido ou deportado de algum país?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="deportado"
    )
    if st.session_state.deportado == "Sim":
        st.text_area(
            "Se sim, descreva:",
            key="detalhes_deportado",
            height=100
        )
