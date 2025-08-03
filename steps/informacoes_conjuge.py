# steps/informacoes_conjuge.py

import streamlit as st
import datetime
import os
import json
from services.path_utils import get_client_data_path


def exibir():
    st.subheader("Informações do Cônjuge")

    # Carrega dados do cliente
    client_id = st.session_state.get("cliente_id", "anonimo")
    caminho = get_client_data_path(client_id)
    dados = {}
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    defaults = dados.get("spouse", {})

    # Nome completo
    st.text_input(
        "Sobrenomes do Cônjuge", 
        value=defaults.get("spouse_surnames", ""),
        key="spouse_surnames"
    )
    st.text_input(
        "Nomes do Cônjuge", 
        value=defaults.get("spouse_given_names", ""),
        key="spouse_given_names"
    )

    # Data de nascimento
    col_dia, col_mes, col_ano = st.columns([1, 1, 1])
    with col_dia:
        st.selectbox(
            "Dia",
            [""] + [f"{d:02d}" for d in range(1, 32)],
            index=["", *[f"{d:02d}" for d in range(1, 32)]].index(defaults.get("spouse_birth_day", "")),
            key="spouse_birth_day"
        )
    with col_mes:
        st.selectbox(
            "Mês",
            ["", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],
            index=["", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"].index(defaults.get("spouse_birth_month", "")),
            key="spouse_birth_month"
        )
    with col_ano:
        st.text_input(
            "Ano",
            value=defaults.get("spouse_birth_year", ""),
            key="spouse_birth_year"
        )
    st.checkbox(
        "Não sei a data de nascimento",
        key="spouse_birth_na",
        value=defaults.get("spouse_birth_na", False)
    )

    # Nacionalidade
    paises = ["", "Brasil", "Afeganistão", "África do Sul", "Alemanha", "Estados Unidos", "Outros…"]
    st.selectbox(
        "País/Região de Origem (Nacionalidade)",
        options=paises,
        index=paises.index(defaults.get("spouse_nationality", "")) if defaults.get("spouse_nationality") in paises else 0,
        key="spouse_nationality"
    )

    # Local de nascimento
    st.markdown("**Local de Nascimento do Cônjuge**")
    st.text_input(
        "Cidade",
        value=defaults.get("spouse_birth_city", ""),
        key="spouse_birth_city"
    )
    st.checkbox(
        "Não sei",
        key="spouse_birth_city_na",
        value=defaults.get("spouse_birth_city_na", False)
    )
    países = ["", "Brasil", "Estados Unidos", "Outro"]
    st.selectbox(
        "País/Região",
        options=países,
        index=países.index(defaults.get("spouse_birth_country", "")) if defaults.get("spouse_birth_country") in países else 0,
        key="spouse_birth_country"
    )

    # Endereço
    st.markdown("**Endereço do Cônjuge**")
    options_addr = ["Escolha…", "Mesmo do Principal", "Outro (especificar)"]
    st.selectbox(
        "Endereço",
        options=options_addr,
        index=options_addr.index(defaults.get("spouse_address_option", "Escolha…")),
        key="spouse_address_option"
    )
    if st.session_state.get("spouse_address_option") == "Outro (especificar)":
        st.text_input(
            "Logradouro (linha 1)",
            value=defaults.get("spouse_addr_line1", ""),
            key="spouse_addr_line1"
        )
        st.text_input(
            "Logradouro (linha 2) *Opcional",
            value=defaults.get("spouse_addr_line2", ""),
            key="spouse_addr_line2"
        )
        st.text_input(
            "Cidade",
            value=defaults.get("spouse_addr_city", ""),
            key="spouse_addr_city"
        )
        col_s1, col_s2 = st.columns([3, 1])
        with col_s1:
            st.text_input(
                "Estado/Província",
                value=defaults.get("spouse_addr_state", ""),
                key="spouse_addr_state"
            )
        with col_s2:
            st.checkbox(
                "Não se aplica",
                key="spouse_addr_state_na",
                value=defaults.get("spouse_addr_state_na", False)
            )
        col_z1, col_z2 = st.columns([3, 1])
        with col_z1:
            st.text_input(
                "CEP/ZIP",
                value=defaults.get("spouse_addr_zip", ""),
                key="spouse_addr_zip"
            )
        with col_z2:
            st.checkbox(
                "Não se aplica",
                key="spouse_addr_zip_na",
                value=defaults.get("spouse_addr_zip_na", False)
            )
        st.selectbox(
            "País/Região",
            options=países,
            index=países.index(defaults.get("spouse_addr_country", "")) if defaults.get("spouse_addr_country") in países else 0,
            key="spouse_addr_country"
        )

    # Botão salvar e próxima etapa
    if st.button("Salvar / Próxima Etapa"):
        # consolida os dados
        dados_spouse = {
            "spouse_surnames":    st.session_state.get("spouse_surnames", ""),
            "spouse_given_names": st.session_state.get("spouse_given_names", ""),
            "spouse_birth_day":   st.session_state.get("spouse_birth_day", ""),
            "spouse_birth_month": st.session_state.get("spouse_birth_month", ""),
            "spouse_birth_year":  st.session_state.get("spouse_birth_year", ""),
            "spouse_birth_na":    st.session_state.get("spouse_birth_na", False),
            "spouse_nationality": st.session_state.get("spouse_nationality", ""),
            "spouse_birth_city":  st.session_state.get("spouse_birth_city", ""),
            "spouse_birth_city_na": st.session_state.get("spouse_birth_city_na", False),
            "spouse_birth_country": st.session_state.get("spouse_birth_country", ""),
            "spouse_address_option": st.session_state.get("spouse_address_option", ""),
            "spouse_addr_line1":   st.session_state.get("spouse_addr_line1", ""),
            "spouse_addr_line2":   st.session_state.get("spouse_addr_line2", ""),
            "spouse_addr_city":    st.session_state.get("spouse_addr_city", ""),
            "spouse_addr_state":   st.session_state.get("spouse_addr_state", ""),
            "spouse_addr_state_na": st.session_state.get("spouse_addr_state_na", False),
            "spouse_addr_zip":    st.session_state.get("spouse_addr_zip", ""),
            "spouse_addr_zip_na": st.session_state.get("spouse_addr_zip_na", False),
            "spouse_addr_country": st.session_state.get("spouse_addr_country", ""),
        }
        # grava no JSON do cliente
        dados["spouse"] = dados_spouse
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        st.success("Informações do cônjuge salvas com sucesso!")
        # define próxima etapa
        st.session_state["etapa"] = "Work / Education / Training Information"
