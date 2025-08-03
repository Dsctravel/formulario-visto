import streamlit as st
import os
import json
from datetime import date, timedelta
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
    st.subheader("Informações de Viagem")
    dados = carregar_dados()

    # 1) Finalidade da viagem
    op_purpose = ["Selecione...", "Visitante de Negócios ou Lazer Temporário (B)", "Estudante Temporário (F)", "Trabalhador Temporário (H)", "Outro"]
    travel_purpose = st.selectbox("Finalidade da viagem aos EUA", op_purpose, index=dados.get("travel_purpose_index", 0))

    # 1.1) Especifique
    op_spec = ["Selecione...", "Negócios ou Turismo (B1/B2)", "Estudos Acadêmicos (F1)", "Ocupação Especial (H1B)", "Outro"]
    travel_specify = st.selectbox("Especifique", op_spec, index=dados.get("travel_specify_index", 0))

    st.markdown("---")

    # 2) Planos específicos
    op_yes_no = ["Selecione...", "Sim", "Não"]
    travel_plans = st.radio("Você fez planos específicos de viagem?", op_yes_no, index=op_yes_no.index(dados.get("travel_plans", "Selecione...")), key="travel_plans")

    st.markdown("### Detalhes de Itinerário")

    # 3) Itinerário
    if travel_plans == "Sim":
        arrival_date = st.date_input("Data de Chegada Prevista", value=date.fromisoformat(dados.get("arrival_date")) if dados.get("arrival_date") else date.today(), key="arrival_date")
        departure_date = st.date_input("Data de Partida Prevista", value=date.fromisoformat(dados.get("departure_date")) if dados.get("departure_date") else date.today(), key="departure_date")
        arrival_flight = st.text_input("Voo de Chegada (se souber)", value=dados.get("arrival_flight", ""), key="arrival_flight")
        arrival_city = st.text_input("Cidade de Chegada", value=dados.get("arrival_city", ""), key="arrival_city")
        departure_flight = st.text_input("Voo de Partida (se souber)", value=dados.get("departure_flight", ""), key="departure_flight")
        departure_city = st.text_input("Cidade de Partida", value=dados.get("departure_city", ""), key="departure_city")
    elif travel_plans == "Não":
        # chegada apenas
        if not st.session_state.get("show_arrival", False):
            if st.button("Selecionar Data de Chegada"): st.session_state.show_arrival = True
            arrival_date = dados.get("arrival_date", "")
        else:
            arrival_date = st.date_input("Data de Chegada Prevista (use data aleatória)", key="arrival_date")
        stay_length = st.text_input("Duração da Estadia (dias)", value=dados.get("stay_length", ""), key="stay_length")
        # endereço pré-preenchido
        st.text_input("Endereço (Linha 1)", value=dados.get("us_contact_street1", "1801 W BUENA VISTA DR"), key="us_contact_street1")
        st.text_input("Endereço (Linha 2) *Opcional", value=dados.get("us_contact_street2", ""), key="us_contact_street2")
        st.text_input("Cidade", value=dados.get("us_contact_city", "ORLANDO"), key="us_contact_city")
        st.selectbox("Estado", ["Selecione...", "FLORIDA"], index=["Selecione...", "FLORIDA"].index(dados.get("us_contact_state", "FLORIDA")), key="us_contact_state")
        st.text_input("CEP (se souber)", value=dados.get("us_contact_zip", "32830"), key="us_contact_zip")
        # não exibe departure picker, será calculado
        departure_date = None
    else:
        arrival_date = dados.get("arrival_date", "")
        departure_date = dados.get("departure_date", "")
        stay_length = dados.get("stay_length", "")

    st.markdown("---")

    # 5) Quem paga?
    op_payer = ["Selecione...", "Eu mesmo", "Parente", "Amigo", "Empregador", "Outro"]
    trip_payer = st.selectbox("Pessoa/Entidade que pagará pela viagem", op_payer, index=dados.get("trip_payer_index", 0), key="trip_payer")
    if trip_payer == "Outro":
        st.subheader("Dados de quem pagará")
        st.text_input("Sobrenome", value=dados.get("payer_lastname", ""), key="payer_lastname")
        st.text_input("Nome", value=dados.get("payer_name", ""), key="payer_name")
        st.text_input("Telefone", value=dados.get("payer_phone", ""), key="payer_phone")
        st.text_input("Email", value=dados.get("payer_email", ""), key="payer_email")
        st.text_input("Relação com você", value=dados.get("payer_relation", ""), key="payer_relation")

    st.markdown("---")

    # Salvar e avançar
    if st.button("Salvar / Próxima Etapa"):
        if travel_plans == "Não" and isinstance(arrival_date, date) and stay_length.isdigit():
            departure_date = arrival_date + timedelta(days=int(stay_length))
        updated = {
            "travel_purpose_index": op_purpose.index(travel_purpose),
            "travel_specify_index": op_spec.index(travel_specify),
            "travel_plans": travel_plans,
            "arrival_date": arrival_date.isoformat() if isinstance(arrival_date, date) else arrival_date,
            "departure_date": departure_date.isoformat() if isinstance(departure_date, date) else (dados.get("departure_date", "")),
            "stay_length": stay_length,
            "us_contact_street1": st.session_state.get("us_contact_street1"),
            "us_contact_street2": st.session_state.get("us_contact_street2"),
            "us_contact_city": st.session_state.get("us_contact_city"),
            "us_contact_state": st.session_state.get("us_contact_state"),
            "us_contact_zip": st.session_state.get("us_contact_zip"),
            "trip_payer_index": op_payer.index(trip_payer),
            # campos extra
            "payer_lastname": st.session_state.get("payer_lastname", ""),
            "payer_name": st.session_state.get("payer_name", ""),
            "payer_phone": st.session_state.get("payer_phone", ""),
            "payer_email": st.session_state.get("payer_email", ""),
            "payer_relation": st.session_state.get("payer_relation", ""),
            "etapa": "Informações de Companheiros de Viagem"
        }
        dados.update(updated)
        salvar_dados(dados)
        st.success("Informações salvas com sucesso.")
        st.session_state.etapa = "Informações de Companheiros de Viagem"
