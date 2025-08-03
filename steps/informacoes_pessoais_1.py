# steps/informacoes_pessoais_1.py

import streamlit as st
from datetime import date
from data.cidades_estados import get_todas_cidades
import json
import os

# Use get_client_data_path para compartilhar o mesmo JSON do formulário principal
from services.path_utils import get_client_data_path

# ─── Funções de I/O ───────────────────────────────────────────
def _load_dados(cliente_id: str):
    path = get_client_data_path(cliente_id)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_dados(cliente_id: str, dados: dict):
    path = get_client_data_path(cliente_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


# ─── Exibição da aba ──────────────────────────────────────────
def exibir():
    st.subheader("Informações Pessoais 1")

    # obtém cliente pela query string
    cliente_id = st.experimental_get_query_params().get("cliente", ["anonimo"])[0]
    dados = _load_dados(cliente_id)

    # Pergunta 0: escolha do Consulado
    consulado_opt = ["", "São Paulo", "Rio de Janeiro", "Recife", "Brasília", "Porto Alegre"]
    consulado = st.selectbox(
        "Consulado onde deseja realizar sua solicitação",
        consulado_opt,
        index=dados.get("consulado_index", 0),
        key="consulado"
    )

    # Pergunta de segurança: primeiro nome da mãe
    nome_mae = st.text_input(
        "Qual o primeiro nome da sua mãe?",
        value=dados.get("primeiro_nome_mae", ""),
        key="primeiro_nome_mae"
    )

    # Sobrenomes e nomes
    sobrenomes = st.text_input(
        "Sobrenomes (como consta no passaporte)",
        value=dados.get("sobrenomes", ""),
        key="sobrenomes"
    )
    nomes = st.text_input(
        "Nomes (como consta no passaporte)",
        value=dados.get("nomes", ""),
        key="nomes"
    )

    # Outros nomes usados
    outros_nomes = st.radio(
        "Você já usou outros nomes (ex: de solteiro, religioso, etc.)?",
        ["Sim", "Não"],
        index={"Sim": 0, "Não": 1}.get(dados.get("outros_nomes", "Não"), 1),
        key="outros_nomes"
    )
    nome_anterior = ""
    if outros_nomes == "Sim":
        nome_anterior = st.text_input(
            "Quais nomes você já usou?",
            value=dados.get("nome_anterior", ""),
            key="nome_anterior"
        )

    # Gênero
    genero = st.radio(
        "Gênero:",
        ["Masculino", "Feminino"],
        index={"Masculino": 0, "Feminino": 1}.get(dados.get("genero", "Masculino"), 0),
        key="genero"
    )

    # Estado civil
    civis = ["", "Casado", "União Estável", "Parceria Doméstica/União Civil",
             "Solteiro", "Viúvo", "Divorciado", "Legalmente Separado", "Outro"]
    estado_civil = st.selectbox(
        "Estado Civil",
        civis,
        index=dados.get("estado_civil_index", 0),
        key="estado_civil"
    )

    # Data de nascimento
    data_nasc_default = None
    if dados.get("data_nascimento"):
        try:
            data_nasc_default = date.fromisoformat(dados["data_nascimento"])
        except:
            data_nasc_default = None
    data_nascimento = st.date_input(
        "Data de Nascimento",
        value=data_nasc_default,
        min_value=date(1930, 1, 1),
        max_value=date.today(),
        format="DD/MM/YYYY",
        key="data_nascimento"
    )

    # Local de nascimento (cidade, estado, país)
    cidades = get_todas_cidades()
    cidade_nascimento = st.selectbox(
        "Cidade de Nascimento",
        [""] + cidades,
        index=dados.get("cidade_nascimento_index", 0),
        key="cidade_nascimento"
    )
    estados = [
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo",
        "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná",
        "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
        "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
    ]
    estado_nascimento = st.selectbox(
        "Estado de Nascimento",
        [""] + estados,
        index=dados.get("estado_nascimento_index", 0),
        key="estado_nascimento"
    )
    paises = ["", "Brasil", "Outro"]
    pais_nascimento = st.selectbox(
        "País de Nascimento",
        paises,
        index=dados.get("pais_nascimento_index", 0),
        key="pais_nascimento"
    )

    # Ação do botão Salvar / Próxima Etapa
    if st.button("Salvar / Próxima Etapa"):
        dados_atualizados = {
            "consulado_index":          consulado_opt.index(consulado),
            "primeiro_nome_mae":        nome_mae,
            "sobrenomes":               sobrenomes,
            "nomes":                    nomes,
            "outros_nomes":             outros_nomes,
            "nome_anterior":            nome_anterior,
            "genero":                   genero,
            "estado_civil_index":       civis.index(estado_civil),
            "data_nascimento":          data_nascimento.isoformat(),
            "cidade_nascimento_index":  cidades.index(cidade_nascimento) if cidade_nascimento else 0,
            "estado_nascimento_index":  estados.index(estado_nascimento) if estado_nascimento else 0,
            "pais_nascimento_index":    paises.index(pais_nascimento),
        }
        _save_dados(cliente_id, dados_atualizados)
        st.success("Informações salvas com sucesso.")
        # avança para a próxima etapa
        st.session_state.etapa = "Informações Pessoais 2"
