# steps/informacoes_conjuge_falecido.py

import streamlit as st
from datetime import date

def exibir():
    st.subheader("Informações de Cônjuge Falecido")

    # 1) Nome completo do cônjuge falecido
    st.text_input("Sobrenomes do Cônjuge Falecido", key="deceased_surname")
    st.text_input("Nomes do Cônjuge Falecido", key="deceased_given_names")

    # Prepara listas de dia, mês, ano e países
    hoje = date.today()
    current_year = hoje.year
    dias = [""] + [f"{d:02d}" for d in range(1, 32)]
    meses = ["", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
    anos = [""] + [str(y) for y in range(current_year, current_year - 101, -1)]
    paises = ["", "Brasil", "Estados Unidos", "Outro"]

    # 2) Data de nascimento
    st.markdown("**Data de Nascimento do Cônjuge Falecido**")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox("Dia", dias, key="deceased_birth_day")
    with c2:
        st.selectbox("Mês", meses, key="deceased_birth_month")
    with c3:
        st.selectbox("Ano", anos, key="deceased_birth_year")
    st.checkbox("Não sei a data de nascimento", key="deceased_birth_na")

    st.markdown("---")

    # 3) Data de falecimento
    st.markdown("**Data de Falecimento**")
    c4, c5, c6 = st.columns(3)
    with c4:
        st.selectbox("Dia", dias, key="deceased_death_day")
    with c5:
        st.selectbox("Mês", meses, key="deceased_death_month")
    with c6:
        st.selectbox("Ano", anos, key="deceased_death_year")
    st.checkbox("Não sei a data de falecimento", key="deceased_death_na")

    st.markdown("---")

    # 4) Nacionalidade
    st.selectbox("Nacionalidade do Cônjuge Falecido", paises, key="deceased_nationality")

    st.markdown("---")

    # 5) Local de falecimento
    st.markdown("**Local de Falecimento**")
    st.text_input("Cidade", key="deceased_death_city")
    st.checkbox("Não sei a cidade de falecimento", key="deceased_death_city_na")
    st.selectbox("País/Região", paises, key="deceased_death_country")
