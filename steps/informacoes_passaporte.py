import streamlit as st
import datetime

def exibir():
    st.header("Informações de Passaporte")

    # 1) Tipo e número do passaporte
    tipos = ["Selecione...", "REGULAR", "DIPLOMÁTICO", "OFICIAL", "OUTRO"]
    st.selectbox("Tipo de Passaporte/Documento de Viagem", tipos, key="passport_type")
    st.text_input("Número do Passaporte/Documento de Viagem", key="passport_number")

    # 2) Número do livro do passaporte (inventory control number)
    st.text_input("Número do Livro do Passaporte", key="passport_book_number")
    st.checkbox("Não se aplica", key="passport_book_na")

    # 3) País/Autoridade emissora
    paises = ["Selecione...", "BRASIL", "ESTADOS UNIDOS", "OUTRO"]
    st.selectbox("País/Autoridade que emitiu o passaporte", paises, key="passport_issuer_country")

    # 4) Local de emissão
    st.subheader("Local de Emissão")
    st.text_input("Cidade", key="passport_issue_city")
    st.text_input("Estado/Província *se constar no passaporte", key="passport_issue_state")
    st.selectbox("País/Região", paises, key="passport_issue_country")

    st.markdown("---")

    # 5) Datas de emissão e expiração com dropdowns
    hoje = datetime.date.today()
    ano_atual = hoje.year

    dias = ["Dia"] + [f"{d:02d}" for d in range(1, 32)]
    meses = ["Mês"] + [
        "JAN", "FEV", "MAR", "ABR", "MAI", "JUN",
        "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"
    ]
    anos = ["Ano"] + [str(y) for y in range(ano_atual - 20, ano_atual + 11)]

    st.subheader("Data de Emissão")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox("Dia", dias, index=0, key="issue_day")
    with c2:
        st.selectbox("Mês", meses, index=0, key="issue_month")
    with c3:
        st.selectbox("Ano", anos, index=0, key="issue_year")

    st.subheader("Data de Expiração")
    st.checkbox("Sem data de expiração", key="no_expiration")
    if not st.session_state.no_expiration:
        c4, c5, c6 = st.columns(3)
        with c4:
            st.selectbox("Dia", dias, index=0, key="expiry_day")
        with c5:
            st.selectbox("Mês", meses, index=0, key="expiry_month")
        with c6:
            st.selectbox("Ano", anos, index=0, key="expiry_year")
