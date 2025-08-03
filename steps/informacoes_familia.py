# steps/informacoes_familia.py

import streamlit as st
import datetime
import os
import json
from services.path_utils import get_client_data_path

def _render_parent(prefix: str, label: str, defaults: dict):
    st.subheader(label)
    # Sobrenomes
    st.text_input(
        "Sobrenomes",
        value=defaults.get("surname", ""),
        key=f"{prefix}_surname"
    )
    st.checkbox("Não sei", key=f"{prefix}_surname_na")

    # Nomes
    st.text_input(
        "Nomes",
        value=defaults.get("given", ""),
        key=f"{prefix}_given"
    )
    st.checkbox("Não sei", key=f"{prefix}_given_na")

    # Data de nascimento (dia/mês/ano)
    hoje = datetime.date.today()
    ano_atual = hoje.year
    dias = ["Dia"] + [f"{d:02d}" for d in range(1, 32)]
    meses = ["Mês", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]
    anos = ["Ano"] + [str(y) for y in range(ano_atual - 100, ano_atual + 1)]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox(
            "Dia",
            dias,
            index=dias.index(defaults.get("day", "Dia")),
            key=f"{prefix}_birth_day"
        )
    with col2:
        st.selectbox(
            "Mês",
            meses,
            index=meses.index(defaults.get("month", "Mês")),
            key=f"{prefix}_birth_month"
        )
    with col3:
        st.selectbox(
            "Ano",
            anos,
            index=anos.index(defaults.get("year", "Ano")),
            key=f"{prefix}_birth_year"
        )

    st.checkbox("Não sei a data de nascimento", key=f"{prefix}_birth_na")

    # Está nos EUA?
    st.radio(
        "Seu pai está nos EUA?" if prefix == "father" else "Sua mãe está nos EUA?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(defaults.get("in_us", "Selecione...")),
        key=f"{prefix}_in_us"
    )

    # Status no país
    options_status = [
        "Selecione...",
        "CIDADÃO AMERICANO",
        "RESIDENTE PERMANENTE LEGAL (LPR)",
        "NÃO IMIGRANTE",
        "OUTRO/NÃO SEI"
    ]
    st.selectbox(
        "Status nos EUA",
        options=options_status,
        index=options_status.index(defaults.get("status", "Selecione...")),
        key=f"{prefix}_status"
    )


def exibir():
    st.header("Informações da Família: Pais")

    # Carrega caminho e dados existentes
    client_id = st.session_state.get("cliente_id", "anonimo")
    caminho = get_client_data_path(client_id)
    dados = {}
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

    # Defaults puxados dos dados salvos (ou vazio)
    defaults_father = dados.get("father", {})
    defaults_mother = dados.get("mother", {})

    # Renderiza blocos dos pais
    _render_parent("father", "Dados do Pai", defaults_father)
    st.markdown("---")
    _render_parent("mother", "Dados da Mãe", defaults_mother)
    st.markdown("---")

    # Parentes imediatos (excluindo pais)
    st.radio(
        "Você tem parentes imediatos, exceto seus pais, nos EUA?",
        options=["Selecione...", "Sim", "Não"],
        index=["Selecione...", "Sim", "Não"].index(dados.get("has_immediate_relatives", "Selecione...")),
        key="has_immediate_relatives"
    )
    immediate_list = dados.get("immediate_relatives", [])
    count = max(1, len(immediate_list))
    if st.session_state.has_immediate_relatives == "Sim":
        st.subheader("Informações dos parentes imediatos")
        for i in range(count):
            rel = immediate_list[i] if i < len(immediate_list) else {}
            st.text_input(f"Sobrenomes #{i+1}", value=rel.get("surname",""), key=f"imm_{i}_surname")
            st.text_input(f"Nomes #{i+1}", value=rel.get("given",""), key=f"imm_{i}_given")
            rel_opts = ["Selecione...", "Cônjuge", "Noivo(a)", "Filho(a)", "Irmão(ã)"]
            st.selectbox(f"Relação #{i+1}", rel_opts, index=rel_opts.index(rel.get("relation","Selecione...")), key=f"imm_{i}_relation")
            status_opts = [
                "Selecione...",
                "CIDADÃO AMERICANO",
                "RESIDENTE PERMANENTE LEGAL (LPR)",
                "NÃO IMIGRANTE",
                "OUTRO/NÃO SEI"
            ]
            st.selectbox(f"Status #{i+1}", status_opts, index=status_opts.index(rel.get("status","Selecione...")), key=f"imm_{i}_status")
            st.markdown("---")

        # botões de adicionar/remover
        col_add, col_remove = st.columns([1,1])
        with col_add:
            if st.button("➕ Adicionar Parente"):
                st.session_state["immediate_count"] = count + 1
        with col_remove:
            if count > 1 and st.button("➖ Remover Parente"):
                st.session_state["immediate_count"] = count - 1

    # Botão salvar e próximo
    if st.button("Salvar / Próxima Etapa"):
        # Reconstitui o dicionário
        dados["father"] = {
            "surname": st.session_state.get("father_surname",""),
            "given":   st.session_state.get("father_given",""),
            "day":     st.session_state.get("father_birth_day",""),
            "month":   st.session_state.get("father_birth_month",""),
            "year":    st.session_state.get("father_birth_year",""),
            "in_us":   st.session_state.get("father_in_us",""),
            "status":  st.session_state.get("father_status",""),
        }
        dados["mother"] = {
            "surname": st.session_state.get("mother_surname",""),
            "given":   st.session_state.get("mother_given",""),
            "day":     st.session_state.get("mother_birth_day",""),
            "month":   st.session_state.get("mother_birth_month",""),
            "year":    st.session_state.get("mother_birth_year",""),
            "in_us":   st.session_state.get("mother_in_us",""),
            "status":  st.session_state.get("mother_status",""),
        }
        dados["has_immediate_relatives"] = st.session_state.get("has_immediate_relatives","Não")

        # reagrupa parentes imediatos
        rels = []
        total = st.session_state.get("immediate_count", count)
        for i in range(total):
            rels.append({
                "surname":  st.session_state.get(f"imm_{i}_surname",""),
                "given":    st.session_state.get(f"imm_{i}_given",""),
                "relation": st.session_state.get(f"imm_{i}_relation",""),
                "status":   st.session_state.get(f"imm_{i}_status",""),
            })
        dados["immediate_relatives"] = rels

        # grava de volta
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        st.success("Informações da família salvas com sucesso!")
        # avança para a próxima etapa
        st.session_state["etapa"] = "Informações do Cônjuge"
