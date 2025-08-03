import streamlit as st

# Etapa Sign and Submit
def exibir():
    st.subheader("Sign and Submit")

    # Número do passaporte para assinatura
    passport_number = st.text_input(
        "Número do Passaporte/Documento de Viagem para assinatura:",
        key="sign_passport_number"
    )

    # Certificação sob perjúrio
    certify = st.checkbox(
        "Eu certifico sob pena de perjúrio sob as leis dos Estados Unidos que as informações fornecidas são verdadeiras e corretas.",
        key="sign_certify"
    )

    # Botão de submissão
    if st.button("Sign and Submit ▶"):
        if not passport_number:
            st.error("Por favor, insira o número do passaporte.")
        elif not certify:
            st.error("Você precisa certificar a declaração para prosseguir.")
        else:
            st.success("Formulário assinado e submetido com sucesso!")
