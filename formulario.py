# formulario.py

import streamlit as st
import smtplib
from email.message import EmailMessage

from steps import (
    informacoes_pessoais_1,
    informacoes_pessoais_2,
    informacoes_viagem,
    informacoes_companheiros,
    informacoes_previas_usa,
    informacoes_endereco_telefone,
    informacoes_contato_eua,
    informacoes_familia,
    informacoes_conjuge,
    informacoes_ex_conjuge,
    informacoes_conjuge_falecido,
    informacoes_trabalho_educacao,
    previous_work_education_training_information as informacoes_trabalho_educacao_previas,
    adicionalwork_education_training    as informacoes_trabalho_educacao_adicional,
    seguranca_antecedentes_parte1       as informacoes_seguranca_1,
    seguranca_antecedentes_parte2       as informacoes_seguranca_2,
    seguranca_antecedentes_parte3       as informacoes_seguranca_3,
    seguranca_antecedentes_parte4       as informacoes_seguranca_4,
    seguranca_antecedentes_parte5       as informacoes_seguranca_5,
    upload_photo                        as informacoes_upload_foto,
    location                            as informacoes_location,
    sign_submit                         as informacoes_sign_submit,
)

st.set_page_config(layout="wide")
st.title("Formulário de Visto")

def send_email(subject: str, body: str, to_address: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"]    = st.secrets["email"]["sender"]
    msg["To"]      = to_address
    msg.set_content(body)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(
            st.secrets["email"]["sender"],
            st.secrets["email"]["password"]
        )
        smtp.send_message(msg)

# 1) Estado inicial
if "etapa" not in st.session_state:
    st.session_state.etapa = "Informações Pessoais 1"

# 2) Abas fixas antes da família
etapas = [
    "Informações Pessoais 1",
    "Informações Pessoais 2",
    "Informações de Viagem",
    "Informações de Companheiros de Viagem",
    "Viagens Anteriores aos EUA",
    "Endereço e Telefone",
    "Contato nos EUA",
    "Informações da Família",
]

# 3) Condicional de cônjuge/ex-cônjuge/cônjuge falecido
marital = st.session_state.get("estado_civil", "").lower()
if marital.startswith("cas"):
    etapas.append("Informações do Cônjuge")
elif marital.startswith("div"):
    etapas.append("Informações de Ex-Cônjuge")
elif marital.startswith("viú") or marital.startswith("viu"):
    etapas.append("Informações de Cônjuge Falecido")

# 4) Abas após família
etapas += [
    "Work / Education / Training Information",
    "Previous Work/Education/Training Information",
    "Additional Work/Education/Training Information",
    "Security and Background Part 1",
    "Security and Background Part 2",
    "Security and Background Part 3",
    "Security and Background Part 4",
    "Security and Background Part 5",
    "Upload Photo",
    "Location Information",
    "Sign and Submit",
]

# 5) Valida etapa
if st.session_state.etapa not in etapas:
    st.session_state.etapa = etapas[0]

# 6) Menu lateral
etapa = st.sidebar.radio(
    "Etapas", etapas, index=etapas.index(st.session_state.etapa)
)
st.session_state.etapa = etapa

# 7) Envio de e-mail manual, em ORDEM fixa
if st.sidebar.button("📧 Enviar respostas por e-mail"):
    # monta assunto
    nome      = st.session_state.get("nomes", "")
    sobrenome = st.session_state.get("sobrenomes", "")
    subject = f"DS-160 Respostas: {nome} {sobrenome}".strip()

    # defina aqui a ordem exata das chaves, conforme o questionário
    ordem_campos = [
        "etapa",
        # Aba 1
        "consulado",
        "primeiro_nome_mae",
        "sobrenomes",
        "nomes",
        "outros_nomes",
        "nome_anterior",
        "genero",
        "estado_civil",
        "data_nascimento",
        "cidade_nascimento",
        "estado_nascimento",
        "pais_nascimento",
        # Aba 2
        "passaporte_numero",
        "passaporte_emissao_dia",
        "passaporte_emissao_mes",
        "passaporte_emissao_ano",
        "passaporte_validade_dia",
        "passaporte_validade_mes",
        "passaporte_validade_ano",
        # Aba 3
        # ... continue listando todas as chaves na ordem exata ...
        # Por fim:
        "upload_status",
        "sign_submit_status"
    ]

    body_lines = []
    # 1) pega as chaves na ordem predefinida
    for chave in ordem_campos:
        if chave in st.session_state:
            body_lines.append(f"{chave}: {st.session_state[chave]}")

    # 2) adiciona qualquer outra chave que não estivesse na lista, ao final
    for chave, valor in st.session_state.items():
        if chave not in ordem_campos:
            body_lines.append(f"{chave}: {valor}")

    body = "\n".join(body_lines) if body_lines else "(nenhum dado preenchido ainda)"

    try:
        send_email(subject, body, st.secrets["email"]["receiver"])
        st.sidebar.success("✅ E-mail enviado com sucesso!")
    except Exception as e:
        st.sidebar.error(f"❌ Falha ao enviar e-mail: {e}")

# 8) Renderiza cada etapa
if   etapa == "Informações Pessoais 1":
    informacoes_pessoais_1.exibir()
elif etapa == "Informações Pessoais 2":
    informacoes_pessoais_2.exibir()
elif etapa == "Informações de Viagem":
    informacoes_viagem.exibir()
elif etapa == "Informações de Companheiros de Viagem":
    informacoes_companheiros.exibir()
elif etapa == "Viagens Anteriores aos EUA":
    informacoes_previas_usa.exibir()
elif etapa == "Endereço e Telefone":
    informacoes_endereco_telefone.exibir()
elif etapa == "Contato nos EUA":
    informacoes_contato_eua.exibir()
elif etapa == "Informações da Família":
    informacoes_familia.exibir()
elif etapa == "Informações do Cônjuge":
    informacoes_conjuge.exibir()
elif etapa == "Informações de Ex-Cônjuge":
    informacoes_ex_conjuge.exibir()
elif etapa == "Informações de Cônjuge Falecido":
    informacoes_conjuge_falecido.exibir()
elif etapa == "Work / Education / Training Information":
    informacoes_trabalho_educacao.exibir()
elif etapa == "Previous Work/Education/Training Information":
    informacoes_trabalho_educacao_previas.exibir()
elif etapa == "Additional Work/Education/Training Information":
    informacoes_trabalho_educacao_adicional.exibir()
elif etapa == "Security and Background Part 1":
    informacoes_seguranca_1.exibir()
elif etapa == "Security and Background Part 2":
    informacoes_seguranca_2.exibir()
elif etapa == "Security and Background Part 3":
    informacoes_seguranca_3.exibir()
elif etapa == "Security and Background Part 4":
    informacoes_seguranca_4.exibir()
elif etapa == "Security and Background Part 5":
    informacoes_seguranca_5.exibir()
elif etapa == "Upload Photo":
    informacoes_upload_foto.exibir()
elif etapa == "Location Information":
    informacoes_location.exibir()
elif etapa == "Sign and Submit":
    informacoes_sign_submit.exibir()
