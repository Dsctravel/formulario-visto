import streamlit as st
import os
import json
from services.path_utils import get_client_data_path

# ─── Funções de I/O ─────────────────────────────────────────
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
    # garante que o diretório exista
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# ─── Exibição da Aba ────────────────────────────────────────
def exibir():
    st.subheader("Informações Pessoais 2")
    dados = carregar_dados()

    # 1) Nacionalidade
    op_nac = ["", "Brasil", "Outro"]
    idx_nac = dados.get("nacionalidade_index", 0)
    nacionalidade = st.selectbox("Nacionalidade", op_nac, index=idx_nac)

    # 2) Outra nacionalidade
    op_sim_nao = ["Sim", "Não"]
    idx_out = op_sim_nao.index(dados.get("tem_outra_nacionalidade", "Não"))
    tem_outra = st.radio("Você possui outra nacionalidade?", op_sim_nao, index=idx_out)
    outra_nac = dados.get("outra_nacionalidade", "") if tem_outra == "Sim" else ""
    if tem_outra == "Sim":
        outra_nac = st.text_input("Qual?", value=outra_nac)

    # 3) Residência permanente fora do Brasil
    idx_res = op_sim_nao.index(dados.get("tem_residencia_permanente", "Não"))
    tem_resid = st.radio(
        "Você possui residência permanente em algum país além do Brasil?",
        op_sim_nao,
        index=idx_res
    )
    pais_resid = dados.get("residencia_pais", "") if tem_resid == "Sim" else ""
    if tem_resid == "Sim":
        pais_resid = st.text_input("Qual país?", value=pais_resid)

    # 4) CPF e RG
    cpf = st.text_input("Número do CPF (se houver)", value=dados.get("cpf", ""))
    rg = st.text_input("Número do RG (se houver)", value=dados.get("rg", ""))

    # 5) Botão de salvar e avançar
    if st.button("Salvar / Próxima Etapa"):
        dados.update({
            "nacionalidade_index": op_nac.index(nacionalidade),
            "tem_outra_nacionalidade": tem_outra,
            "outra_nacionalidade": outra_nac,
            "tem_residencia_permanente": tem_resid,
            "residencia_pais": pais_resid,
            "cpf": cpf,
            "rg": rg,
            # registra a próxima etapa
            "etapa": "Informações de Viagem"
        })
        salvar_dados(dados)
        st.success("Informações salvas com sucesso.")
        # atualiza fluxo
        st.session_state.etapa = "Informações de Viagem"
