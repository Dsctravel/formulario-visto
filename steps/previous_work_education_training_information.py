# steps/previous_work_education_training_information.py

import streamlit as st
from datetime import date
import json
import os
# —– Removido: import selenium —— 

# caso você carregue ou salve valores em JSON, mantenha essas constantes:
DATA_DIR = "dados_clientes"
os.makedirs(DATA_DIR, exist_ok=True)
CAMINHO_JSON = os.path.join(DATA_DIR, "previous_work.json")

def carregar_dados():
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

dados = carregar_dados()

def exibir():
    st.subheader("Previous Work/Education/Training Information")

    # Pergunta: Were you previously employed?
    prev_emp = st.radio(
        "Were you previously employed?",
        ["Yes", "No"],
        index=0 if dados.get("prev_emp") is None else (0 if dados["prev_emp"] == "Yes" else 1),
        key="prev_emp"
    )
    if st.session_state.prev_emp == "Yes":
        st.text_input("Employer Name", value=dados.get("employer_name", ""), key="employer_name")
        st.text_input("Employer Street Address (Line 1)", value=dados.get("emp_street1", ""), key="emp_street1")
        st.text_input("Employer Street Address (Line 2) *Optional", value=dados.get("emp_street2", ""), key="emp_street2")
        st.text_input("City", value=dados.get("emp_city", ""), key="emp_city")
        col1, col2 = st.columns([3,1])
        with col1:
            st.text_input("State/Province", value=dados.get("emp_state", ""), key="emp_state")
        with col2:
            st.checkbox("Does Not Apply", value=dados.get("emp_state_na", False), key="emp_state_na")
        col3, col4 = st.columns([3,1])
        with col3:
            st.text_input("Postal Zone/ZIP Code", value=dados.get("emp_zip", ""), key="emp_zip")
        with col4:
            st.checkbox("Does Not Apply", value=dados.get("emp_zip_na", False), key="emp_zip_na")
        st.selectbox(
            "Country/Region",
            options=["","Brazil","United States","Other"],
            index=["","Brazil","United States","Other"].index(dados.get("emp_country","")),
            key="emp_country"
        )
        st.text_input("Job Title", value=dados.get("job_title", ""), key="job_title")
        st.text_input("Supervisor's Surname", value=dados.get("sup_surname", ""), key="sup_surname")
        st.checkbox("Do Not Know", value=dados.get("sup_surname_na", False), key="sup_surname_na")
        st.text_input("Supervisor's Given Names", value=dados.get("sup_given", ""), key="sup_given")
        st.checkbox("Do Not Know", value=dados.get("sup_given_na", False), key="sup_given_na")
        st.date_input(
            "Employment Date From",
            value=date.fromisoformat(dados.get("emp_date_from","2000-01-01")),
            key="emp_date_from"
        )
        st.date_input(
            "Employment Date To",
            value=date.fromisoformat(dados.get("emp_date_to","2000-01-01")),
            key="emp_date_to"
        )
        st.text_area("Briefly describe your duties:", value=dados.get("duties",""), key="duties")

    # Pergunta: educational institutions?
    edu = st.radio(
        "Have you attended any educational institutions at a secondary level or above?",
        ["Yes", "No"],
        index=0 if dados.get("edu") is None else (0 if dados["edu"]=="Yes" else 1),
        key="edu"
    )
    if st.session_state.edu == "Yes":
        st.text_input("Name of Institution", value=dados.get("inst_name",""), key="inst_name")
        st.text_input("Street Address (Line 1)", value=dados.get("inst_street1",""), key="inst_street1")
        st.text_input("Street Address (Line 2) *Optional", value=dados.get("inst_street2",""), key="inst_street2")
        st.text_input("City", value=dados.get("inst_city",""), key="inst_city")
        col5, col6 = st.columns([3,1])
        with col5:
            st.text_input("State/Province", value=dados.get("inst_state",""), key="inst_state")
        with col6:
            st.checkbox("Does Not Apply", value=dados.get("inst_state_na",False), key="inst_state_na")
        col7, col8 = st.columns([3,1])
        with col7:
            st.text_input("Postal Zone/ZIP Code", value=dados.get("inst_zip",""), key="inst_zip")
        with col8:
            st.checkbox("Does Not Apply", value=dados.get("inst_zip_na",False), key="inst_zip_na")
        st.selectbox(
            "Country/Region",
            options=["","Brazil","United States","Other"],
            index=["","Brazil","United States","Other"].index(dados.get("inst_country","")),
            key="inst_country"
        )
        st.text_input("Course of Study", value=dados.get("course",""), key="course")
        st.date_input("Date of Attendance From", value=date.fromisoformat(dados.get("att_from","2000-01-01")), key="att_from")
        st.date_input("Date of Attendance To",   value=date.fromisoformat(dados.get("att_to","2000-01-01")),   key="att_to")

    # Botão para salvar e avançar
    if st.button("Salvar / Próxima Etapa"):
        novos = {
            "prev_emp":                 st.session_state.prev_emp,
            "employer_name":            st.session_state.get("employer_name",""),
            "emp_street1":              st.session_state.get("emp_street1",""),
            "emp_street2":              st.session_state.get("emp_street2",""),
            "emp_city":                 st.session_state.get("emp_city",""),
            "emp_state":                st.session_state.get("emp_state",""),
            "emp_state_na":             st.session_state.get("emp_state_na",False),
            "emp_zip":                  st.session_state.get("emp_zip",""),
            "emp_zip_na":               st.session_state.get("emp_zip_na",False),
            "emp_country":              st.session_state.get("emp_country",""),
            "job_title":                st.session_state.get("job_title",""),
            "sup_surname":              st.session_state.get("sup_surname",""),
            "sup_surname_na":           st.session_state.get("sup_surname_na",False),
            "sup_given":                st.session_state.get("sup_given",""),
            "sup_given_na":             st.session_state.get("sup_given_na",False),
            "emp_date_from":            st.session_state.get("emp_date_from",""),
            "emp_date_to":              st.session_state.get("emp_date_to",""),
            "duties":                   st.session_state.get("duties",""),
            "edu":                      st.session_state.edu,
            "inst_name":                st.session_state.get("inst_name",""),
            "inst_street1":             st.session_state.get("inst_street1",""),
            "inst_street2":             st.session_state.get("inst_street2",""),
            "inst_city":                st.session_state.get("inst_city",""),
            "inst_state":               st.session_state.get("inst_state",""),
            "inst_state_na":            st.session_state.get("inst_state_na",False),
            "inst_zip":                 st.session_state.get("inst_zip",""),
            "inst_zip_na":              st.session_state.get("inst_zip_na",False),
            "inst_country":             st.session_state.get("inst_country",""),
            "course":                   st.session_state.get("course",""),
            "att_from":                 st.session_state.get("att_from",""),
            "att_to":                   st.session_state.get("att_to",""),
        }
        salvar_dados(novos)
        st.success("Dados anteriores salvos com sucesso.")
        st.session_state.etapa = "Additional Work/Education/Training Information"
