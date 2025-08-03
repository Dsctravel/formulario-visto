# steps/informacoes_trabalho_educacao.py

import streamlit as st
import datetime

def exibir():
    st.header("Informações de Trabalho/Estudo Atual")
    st.markdown("**NOTE:** Forneça as informações sobre seu emprego ou estudo atual.")

    # 1) Ocupação principal
    ocupacoes = [
        "- SELECIONE -",
        "AGRICULTURA",
        "ARTISTA/PERFORMER",
        "NEGÓCIOS",
        "COMUNICAÇÕES",
        "CIÊNCIA DA COMPUTAÇÃO",
        "GASTRONOMIA",
        "EDUCAÇÃO",
        "ENGENHARIA",
        "GOVERNO",
        "DONO DE CASA",
        "PROFISSÃO JURÍDICA",
        "SAÚDE",
        "MILITAR",
        "CIÊNCIAS NATURAIS",
        "DESEMPREGADO(A)",
        "CIÊNCIAS FÍSICAS",
        "VOCACÃO RELIGIOSA",
        "PESQUISA",
        "APOSENTADO(A)",
        "CIÊNCIAS SOCIAIS",
        "ESTUDANTE",
        "OUTRO",
    ]
    st.selectbox("Ocupação Principal", ocupacoes, index=0, key="occupation")

    # 2) Nome do empregador ou escola
    st.text_input("Nome da Empresa ou Escola", value="", key="employer_name")

    # 3) Endereço do empregador/escola
    st.subheader("Endereço da Empresa/Escola")
    st.text_input("Endereço (Linha 1)", value="", key="employer_addr1")
    st.text_input("Endereço (Linha 2) *Opcional", value="", key="employer_addr2")
    st.text_input("Cidade", value="", key="employer_city")
    col_state, col_state_na = st.columns([3,1])
    with col_state:
        st.text_input("Estado/Província", value="", key="employer_state")
    with col_state_na:
        st.checkbox("Não se aplica", key="employer_state_na")
    col_zip, col_zip_na = st.columns([3,1])
    with col_zip:
        st.text_input("Código Postal", value="", key="employer_zip")
    with col_zip_na:
        st.checkbox("Não se aplica", key="employer_zip_na")
    st.selectbox(
        "País/Região",
        ["- SELECIONE -", "BRASIL", "ESTADOS UNIDOS", "OUTRO"],
        index=0,
        key="employer_country"
    )

    # 4) Data de início (20 anos atrás → 10 anos à frente)
    st.subheader("Data de Início")
    hoje = datetime.date.today()
    ano_atual = hoje.year
    dias = ["Dia"] + [f"{d:02d}" for d in range(1, 32)]
    meses = ["Mês", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
    anos = ["Ano"] + [str(y) for y in range(ano_atual - 20, ano_atual + 11)]

    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox("Dia", dias, index=0, key="start_day")
    with c2:
        st.selectbox("Mês", meses, index=0, key="start_month")
    with c3:
        st.selectbox("Ano", anos, index=0, key="start_year")
    st.caption("(Formato: DD-MMM-YYYY)")

    # 5) Renda mensal
    col_inc, col_inc_na = st.columns([3,1])
    with col_inc:
        st.text_input("Renda Mensal em Moeda Local (se empregado)", value="", key="monthly_income")
    with col_inc_na:
        st.checkbox("Não se aplica", key="monthly_income_na")

    # 6) Descrição das funções
    st.text_area("Descreva brevemente suas funções", value="", key="job_description", height=100)
