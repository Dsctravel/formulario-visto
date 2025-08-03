# steps/informacoes_companheiros.py

import streamlit as st
import json
import os
from services.path_utils import get_client_data_path

# ─── Helpers para carregar e salvar JSON ───────────────────────
def carregar_dados():
    cliente = st.experimental_get_query_params().get("cliente", ["anonimo"])[0]
    path = get_client_data_path(cliente)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    cliente = st.experimental_get_query_params().get("cliente", ["anonimo"])[0]
    path = get_client_data_path(cliente)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# ─── Exibição da aba ──────────────────────────────────────────
def exibir():
    st.subheader("Informações de Companheiros de Viagem")
    dados = carregar_dados()

    # 1) Há outras pessoas viajando com você?
    opts_comp = ["Selecione...", "Sim", "Não"]
    idx_comp = dados.get("travel_companions_index", 0)
    travel_companions = st.radio(
        "Há outras pessoas viajando com você?",
        options=opts_comp,
        index=idx_comp,
        key="travel_companions"
    )

    # Se não há ninguém, permite salvar e volta
    if travel_companions == "Não":
        if st.button("Salvar / Próxima Etapa"):
            dados_atualizado = {
                **dados,
                "travel_companions_index": opts_comp.index(travel_companions)
            }
            salvar_dados(dados_atualizado)
            st.success("Informações salvas com sucesso.")
            st.session_state.etapa = "Viagens Anteriores aos EUA"
        return

    # 2) Você está viajando como parte de um grupo?
    opts_group = ["Selecione...", "Sim", "Não"]
    idx_grp = dados.get("travel_group_index", 0)
    travel_group = st.radio(
        "Você está viajando como parte de um grupo ou organização?",
        options=opts_group,
        index=idx_grp,
        key="travel_group"
    )

    # estados iniciais de campo
    group_name       = dados.get("group_name", "")
    comp_surname     = dados.get("comp_surname", "")
    comp_given_name  = dados.get("comp_given_name", "")
    relationship_opts = [
        "Selecione...",
        "Pai/Mãe",
        "Cônjuge",
        "Filho(a)",
        "Outro Parente",
        "Amigo(a)",
        "Parceiro de Negócios",
        "Outro"
    ]
    idx_rel = dados.get("comp_relationship_index", 0)

    # 2.1) Se for grupo, nome da organização
    if travel_group == "Sim":
        group_name = st.text_input(
            "Nome do grupo ou organização",
            value=group_name,
            key="group_name"
        )

    # 2.2) Se não, dados de cada pessoa
    else:
        st.subheader("Dados da(s) pessoa(s) viajando com você")
        comp_surname = st.text_input(
            "Sobrenomes da pessoa viajando com você",
            value=comp_surname,
            key="comp_surname"
        )
        comp_given_name = st.text_input(
            "Nomes da pessoa viajando com você",
            value=comp_given_name,
            key="comp_given_name"
        )
        idx_rel = st.selectbox(
            "Parentesco com a pessoa",
            options=relationship_opts,
            index=idx_rel,
            key="comp_relationship"
        )

    # 3) Botão de salvar / próxima etapa
    if st.button("Salvar / Próxima Etapa"):
        dados_atualizado = {
            **dados,
            "travel_companions_index":    opts_comp.index(travel_companions),
            "travel_group_index":         opts_group.index(travel_group),
            "group_name":                 group_name,
            "comp_surname":               comp_surname,
            "comp_given_name":            comp_given_name,
            "comp_relationship_index":    idx_rel
        }
        salvar_dados(dados_atualizado)
        st.success("Informações salvas com sucesso.")
        st.session_state.etapa = "Viagens Anteriores aos EUA"
