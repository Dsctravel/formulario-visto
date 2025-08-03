import streamlit as st
import os
import json
from datetime import date
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
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# ─── Exibição da Aba ────────────────────────────────────────
def exibir():
    st.header("Informações de Viagens Anteriores aos EUA")
    dados = carregar_dados()

    # 1) Já esteve nos EUA?
    prev_ever = st.radio(
        "Você já esteve nos EUA?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(dados.get("prev_ever_been", "Selecione...")),
        key="prev_ever_been"
    )
    if prev_ever == "Sim":
        st.subheader("Detalhes da(s) visita(s)")
        prev_visit_date = st.date_input(
            "Data da Chegada",
            value=date.fromisoformat(dados.get("prev_visit_date")) if dados.get("prev_visit_date") else None,
            key="prev_visit_date"
        )
        prev_visit_length = st.text_input(
            "Tempo de permanência (dias)",
            value=dados.get("prev_visit_length", ""),
            key="prev_visit_length"
        )

    st.markdown("---")

    # 2) Já teve visto americano?
    prev_visa = st.radio(
        "Você já recebeu um visto americano?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_issued", "Selecione...")),
        key="prev_visa_issued"
    )
    if prev_visa == "Sim":
        st.subheader("Detalhes do último visto")
        prev_visa_date = st.date_input(
            "Data de emissão do último visto",
            value=date.fromisoformat(dados.get("prev_visa_date")) if dados.get("prev_visa_date") else None,
            key="prev_visa_date"
        )
        prev_visa_number = st.text_input(
            "Número do visto",
            value=dados.get("prev_visa_number", ""),
            placeholder="Se não souber, deixe em branco e marque a caixa",
            key="prev_visa_number"
        )
        prev_visa_unknown = st.checkbox(
            "Não sei o número do visto",
            value=dados.get("prev_visa_number_unknown", False),
            key="prev_visa_number_unknown"
        )
        st.radio(
            "Você está solicitando o mesmo tipo de visto?",
            options=["Selecione...", "Sim", "Não"],
            index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_same_type", "Selecione...")),
            key="prev_visa_same_type"
        )
        st.radio(
            "Solicitando no mesmo país/local onde foi emitido e onde reside?",
            options=["Selecione...", "Sim", "Não"],
            index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_same_place", "Selecione...")),
            key="prev_visa_same_place"
        )
        st.radio(
            "Você já forneceu impressões digitais (ten-print)?",
            options=["Selecione...", "Sim", "Não"],
            index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_ten_printed", "Selecione...")),
            key="prev_visa_ten_printed"
        )
        st.radio(
            "Seu visto já foi perdido ou roubado?",
            options=["Selecione...", "Sim", "Não"],
            index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_lost", "Selecione...")),
            key="prev_visa_lost"
        )
        st.radio(
            "Seu visto já foi cancelado ou revogado?",
            options=["Selecione...", "Sim", "Não"],
            index=["Selecione...", "Sim", "Não"].index(dados.get("prev_visa_revoked", "Selecione...")),
            key="prev_visa_revoked"
        )

    st.markdown("---")

    # 3) Negado/retirado?
    prev_refusal = st.radio(
        "Visto negado, admissão negada ou retirada de pedido?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(dados.get("prev_refusal", "Selecione...")),
        key="prev_refusal"
    )
    if prev_refusal == "Sim":
        prev_refusal_explain = st.text_area(
            "Explique o ocorrido",
            value=dados.get("prev_refusal_explain", ""),
            key="prev_refusal_explain"
        )

    st.markdown("---")

    # 4) Petição de imigração?
    prev_petition = st.radio(
        "Alguém apresentou petição de imigração em seu nome?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(dados.get("prev_immigration_petition", "Selecione...")),
        key="prev_immigration_petition"
    )
    if prev_petition == "Sim":
        prev_petition_explain = st.text_area(
            "Explique quem e quando",
            value=dados.get("prev_immigration_petition_explain", ""),
            key="prev_immigration_petition_explain"
        )

    st.markdown("---")

    # Botão de salvar e avançar
    if st.button("Salvar / Próxima Etapa"):
        # Coleta todos os campos no dicionário
        dados.update({
            "prev_ever_been": prev_ever,
            "prev_visit_date": (prev_visit_date.isoformat() if 'prev_visit_date' in st.session_state and isinstance(st.session_state.prev_visit_date, date) else dados.get("prev_visit_date", "")),
            "prev_visit_length": st.session_state.get("prev_visit_length", ""),
            "prev_visa_issued": prev_visa,
            "prev_visa_date": (st.session_state.prev_visa_date.isoformat() if 'prev_visa_date' in st.session_state and isinstance(st.session_state.prev_visa_date, date) else dados.get("prev_visa_date", "")),
            "prev_visa_number": st.session_state.get("prev_visa_number", ""),
            "prev_visa_number_unknown": st.session_state.get("prev_visa_number_unknown", False),
            "prev_visa_same_type": st.session_state.get("prev_visa_same_type", ""),
            "prev_visa_same_place": st.session_state.get("prev_visa_same_place", ""),
            "prev_visa_ten_printed": st.session_state.get("prev_visa_ten_printed", ""),
            "prev_visa_lost": st.session_state.get("prev_visa_lost", ""),
            "prev_visa_revoked": st.session_state.get("prev_visa_revoked", ""),
            "prev_refusal": prev_refusal,
            "prev_refusal_explain": st.session_state.get("prev_refusal_explain", ""),
            "prev_immigration_petition": prev_petition,
            "prev_immigration_petition_explain": st.session_state.get("prev_immigration_petition_explain", ""),
            # Define a próxima etapa abaixo:
            "etapa": "Informações de Companheiros de Viagem"
        })
        salvar_dados(dados)
        st.success("Informações anteriores salvas com sucesso.")
        st.session_state.etapa = "Informações de Companheiros de Viagem"
