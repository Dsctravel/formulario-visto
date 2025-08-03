# steps/informacoes_ex_conjuge.py

import streamlit as st
from datetime import date

def exibir():
    st.header("Family Information: Former Spouse")

    # 1) Quantos ex-cônjuges
    count = st.session_state.get("former_count", 0)
    count = st.number_input(
        "Number of Former Spouses:",
        min_value=0,
        value=count,
        step=1,
        key="former_count"
    )

    # listas reutilizáveis
    days   = [""] + [f"{d:02d}" for d in range(1, 32)]
    months = ["","JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"]
    year_now = date.today().year
    years  = [""] + [str(y) for y in range(year_now, year_now-100, -1)]
    countries = [
        "", "Brasil", "Estados Unidos", "Canadá", "México",
        "Reino Unido", "França", "Alemanha", "Japão", "China",
        "Índia", "Austrália", "Outro"
    ]

    # 2) Para cada ex-cônjuge, renderiza o bloco
    for i in range(count):
        st.subheader(f"Former Spouse #{i+1} Information")

        # nomes
        st.text_input("Surnames", key=f"former_{i}_surname")
        st.text_input("Given Names", key=f"former_{i}_given")

        # data de nascimento
        col_d, col_m, col_y = st.columns(3)
        with col_d:
            st.selectbox("Day", days, key=f"former_{i}_birth_day")
        with col_m:
            st.selectbox("Month", months, key=f"former_{i}_birth_month")
        with col_y:
            st.text_input("Year", key=f"former_{i}_birth_year")

        # nacionalidade
        st.selectbox(
            "Country/Region of Origin (Nationality)",
            options=countries,
            key=f"former_{i}_nationality"
        )

        # local de nascimento
        with st.expander("Place of Birth"):
            st.text_input("City", key=f"former_{i}_birth_city")
            st.checkbox("Do Not Know", key=f"former_{i}_birth_city_na")
            st.selectbox(
                "Country/Region",
                options=countries,
                key=f"former_{i}_birth_country"
            )

        # data de casamento
        col_md, col_mm, col_my = st.columns(3)
        with col_md:
            st.selectbox("Marriage Day", days, key=f"former_{i}_marriage_day")
        with col_mm:
            st.selectbox("Marriage Month", months, key=f"former_{i}_marriage_month")
        with col_my:
            st.text_input("Marriage Year", key=f"former_{i}_marriage_year")

        # data término
        col_ed, col_em, col_ey = st.columns(3)
        with col_ed:
            st.selectbox("End Day", days, key=f"former_{i}_end_day")
        with col_em:
            st.selectbox("End Month", months, key=f"former_{i}_end_month")
        with col_ey:
            st.text_input("End Year", key=f"former_{i}_end_year")

        # motivo do término
        st.text_area(
            "How the Marriage Ended",
            height=100,
            key=f"former_{i}_end_reason"
        )

        # país onde o casamento foi terminado
        st.selectbox(
            "Country/Region Marriage was Terminated",
            options=countries,
            key=f"former_{i}_end_country"
        )

        st.markdown("---")

    # 3) Controles de adicionar/remover
    col_add, col_rem = st.columns(2)
    with col_add:
        if st.button("➕ Add Another"):
            st.session_state.former_count = count + 1
    with col_rem:
        if count > 0 and st.button("➖ Remove"):
            st.session_state.former_count = count - 1

    # 4) Botão de salvar/avançar (se estiver integrando com o fluxo principal)
    if st.button("Salvar / Próxima Etapa"):
        st.success("Informações de ex-cônjuge salvas com sucesso!")
