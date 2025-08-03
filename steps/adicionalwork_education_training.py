# steps/addicionalwork_education_training.py

import streamlit as st
import os
import json
from services.path_utils import get_client_data_path

# Additional Work/Education/Training Information

def exibir():
    st.header("Additional Work/Education/Training Information")
    st.markdown(
        "**NOTE:** Provide complete and accurate information for each question."
    )

    # Identifica o cliente e carrega dados
    client_id = st.session_state.get(
        "cliente_id",
        st.experimental_get_query_params().get("cliente", ["anonimo"])[0]
    )
    path = get_client_data_path(client_id)
    dados = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
    defaults = dados.get("additional_work", {})

    # 1) Clan/tribe
    clan_opts = ("No", "Yes")
    clan_default = defaults.get("clan", "No")
    clan_index = clan_opts.index(clan_default) if clan_default in clan_opts else 0
    clan = st.radio(
        "Do you belong to a clan or tribe?",
        clan_opts,
        index=clan_index,
        key="clan"
    )

    st.markdown("---")

    # 2) Languages spoken (dinâmico)
    st.markdown("**Provide a List of Languages You Speak**")
    default_langs = defaults.get("languages", [])
    if "lang_count" not in st.session_state:
        st.session_state.lang_count = len(default_langs) or 1
    for i in range(st.session_state.lang_count):
        default_val = default_langs[i] if i < len(default_langs) else ""
        st.text_input(
            f"Language #{i+1}",
            value=default_val,
            key=f"language_{i}"
        )
    col_add, col_rem = st.columns([1,1])
    with col_add:
        if st.button("➕ Add Another Language"):
            st.session_state.lang_count += 1
    with col_rem:
        if st.session_state.lang_count > 1 and st.button("➖ Remove Language"):
            st.session_state.lang_count -= 1

    st.markdown("---")

    # 3) Travel in last five years
    travel_opts = ("No", "Yes")
    travel_default = defaults.get("travel", "No")
    travel_index = travel_opts.index(travel_default) if travel_default in travel_opts else 0
    travel = st.radio(
        "Have you traveled to any countries/regions within the last five years?",
        travel_opts,
        index=travel_index,
        key="travel"
    )
    if travel == "Yes":
        country_choices = [
            "- SELECT ONE -",
            "United States", "Canada", "Brazil", "United Kingdom",
            "France", "Germany", "Spain", "Italy", "Japan",
            "Australia", "India", "China", "Mexico"
        ]
        default_countries = defaults.get("countries", [])
        if "country_count" not in st.session_state:
            st.session_state.country_count = len(default_countries) or 1
        for i in range(st.session_state.country_count):
            default_ctry = default_countries[i] if i < len(default_countries) else "- SELECT ONE -"
            st.selectbox(
                f"Country/Region Visited #{i+1}",
                options=country_choices,
                index=country_choices.index(default_ctry) if default_ctry in country_choices else 0,
                key=f"country_{i}"
            )
        col_add_ct, col_rem_ct = st.columns([1,1])
        with col_add_ct:
            if st.button("➕ Add Another Country"):
                st.session_state.country_count += 1
        with col_rem_ct:
            if st.session_state.country_count > 1 and st.button("➖ Remove Country"):
                st.session_state.country_count -= 1

    st.markdown("---")

    # 4) Professional/social/charitable organization
    org_opts = ("No", "Yes")
    org_default = defaults.get("org", "No")
    org_index = org_opts.index(org_default) if org_default in org_opts else 0
    org = st.radio(
        "Have you belonged to, contributed to, or worked for any professional, social, or charitable organization?",
        org_opts,
        index=org_index,
        key="org"
    )
    if org == "Yes":
        st.text_area(
            "If yes, please describe which organization(s)",
            value=defaults.get("org_details", ""),
            key="org_details",
            height=100
        )

    st.markdown("---")

    # 5) Specialized skills/training
    skills_opts = ("No", "Yes")
    skills_default = defaults.get("skills", "No")
    skills_index = skills_opts.index(skills_default) if skills_default in skills_opts else 0
    skills = st.radio(
        "Do you have any specialized skills or training, such as firearms, explosives, nuclear, biological, or chemical experience?",
        skills_opts,
        index=skills_index,
        key="skills"
    )
    if skills == "Yes":
        st.text_area(
            "If yes, please describe",
            value=defaults.get("skills_details", ""),
            key="skills_details",
            height=100
        )

    st.markdown("---")

    # 6) Military service
    mil_opts = ("No", "Yes")
    mil_default = defaults.get("military", "No")
    mil_index = mil_opts.index(mil_default) if mil_default in mil_opts else 0
    military = st.radio(
        "Have you ever served in the military?",
        mil_opts,
        index=mil_index,
        key="military"
    )
    if military == "Yes":
        st.text_area(
            "If yes, please describe where and when",
            value=defaults.get("military_details", ""),
            key="military_details",
            height=100
        )

    st.markdown("---")

    # 7) Paramilitary/insurgent service
    param_opts = ("No", "Yes")
    param_default = defaults.get("paramil", "No")
    param_index = param_opts.index(param_default) if param_default in param_opts else 0
    paramil = st.radio(
        "Have you ever served in, been a member of, or been involved with a paramilitary unit, vigilante unit, rebel group, guerrilla group, or insurgent organization?",
        param_opts,
        index=param_index,
        key="paramil"
    )
    if paramil == "Yes":
        st.text_area(
            "If yes, please describe",
            value=defaults.get("paramil_details", ""),
            key="paramil_details",
            height=100
        )

    st.markdown("---")

    # Salvar e próxima etapa
    if st.button("Salvar / Próxima Etapa"):
        updated = dados.get("additional_work", {})
        updated.update({
            "clan": clan,
            "languages": [st.session_state.get(f"language_{i}", "") for i in range(st.session_state.lang_count)],
            "travel": travel,
            "countries": [st.session_state.get(f"country_{i}", "") for i in range(st.session_state.country_count)] if travel == "Yes" else [],
            "org": org,
            "org_details": st.session_state.get("org_details", ""),
            "skills": skills,
            "skills_details": st.session_state.get("skills_details", ""),
            "military": military,
            "military_details": st.session_state.get("military_details", ""),
            "paramil": paramil,
            "paramil_details": st.session_state.get("paramil_details", ""),
        })
        dados["additional_work"] = updated
        with open(path, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        st.success("Additional work/education/training information saved.")
        # Avança para próxima etapa
        st.session_state["etapa"] = "Security and Background Part 1"
