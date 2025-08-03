import streamlit as st
import os
import json
from datetime import date
from services.path_utils import get_client_data_path

# --- Carrega dados existentes do cliente ---
client_id = st.session_state.get("client_id", "default")
data_path = get_client_data_path(client_id)
if os.path.exists(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        client_data = json.load(f)
else:
    client_data = {}

st.title("Detalhes de Itinerário")
st.subheader("Você fez planos específicos de viagem?")

plans = st.radio(
    "",
    ("Selecione...", "Sim", "Não"),
    index=0,
    key="viagem_plano_especifico"
)

if plans == "Não":
    # calendário em branco
    arrival_date = st.date_input(
        "Data de Chegada Prevista (pode usar uma data aleatória)",
        value=None,
        key="data_chegada"
    )

    stay_duration = st.number_input(
        "Duração da Estadia (dias)",
        min_value=1,
        step=1,
        key="duracao_estadia"
    )

    st.markdown("---")
    st.subheader("Endereço nos EUA (pré-preenchido)")

    us_address = st.text_input(
        "Endereço",
        value="1801 W Buena Vista Dr",
        key="us_endereco"
    )
    us_city = st.text_input(
        "Cidade",
        value="Lake Buena Vista",
        key="us_cidade"
    )
    us_state = st.text_input(
        "Estado",
        value="FL",
        key="us_estado"
    )
    us_zip = st.text_input(
        "CEP",
        value="32830",
        key="us_cep"
    )

    if st.button("Salvar e Próxima Etapa"):
        client_data["viagem_plano_especifico"] = False
        client_data["data_chegada"] = (
            arrival_date.isoformat() if isinstance(arrival_date, date) else None
        )
        client_data["duracao_estadia_dias"] = stay_duration
        client_data["endereco_eua"] = {
            "endereco": us_address,
            "cidade": us_city,
            "estado": us_state,
            "cep": us_zip,
        }
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(client_data, f, ensure_ascii=False, indent=2)

        st.session_state.etapa = "proxima_aba"
        st.experimental_rerun()

elif plans == "Sim":
    st.info("Ótimo! Então você poderá informar aqui seus planos específicos de viagem.")
