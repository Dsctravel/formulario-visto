import streamlit as st

def exibir():
    st.subheader("Segurança e Antecedentes - Parte 5")

    # 1) Retenção de custódia de criança cidadã dos EUA
    st.radio(
        'Você já reteve custódia de uma criança cidadã dos EUA fora dos Estados Unidos de uma pessoa que recebeu custódia legal por um tribunal dos EUA?',
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="reteve_custodia"
    )

    # 2) Voto ilegal nos EUA
    st.radio(
        'Você já votou nos Estados Unidos em violação de qualquer lei ou regulamento?',
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="voto_ilegal"
    )

    # 3) Renúncia de cidadania para evitar tributação
    st.radio(
        'Você já renunciou à cidadania dos Estados Unidos com o propósito de evitar tributação?',
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="renunciou_cidadania"
    )
