# steps/seguranca_antecedentes_partes1.py
import streamlit as st

def exibir():
    st.header("Security and Background: Part 1")
    st.markdown(
        "NOTE: Provide the following security and background information. "
        "Provide complete and accurate information to all questions that require an explanation. "
        "A visa may not be issued to persons who are within specific categories defined by law as "
        "inadmissible to the United States (except when a waiver is obtained in advance). Are any of the "
        "following applicable to you? While a YES answer does not automatically signify ineligibility for a "
        "visa, if you answer YES you may be required to personally appear before a consular officer."
    )

    q1 = st.radio(
        "Do you have a communicable disease of public health significance?",
        ("No", "Yes"),
        index=0,
        key="disease_public_health"
    )
    if q1 == "Yes":
        st.text_area("If yes, please explain", key="disease_public_health_details", height=100)

    st.markdown("---")
    q2 = st.radio(
        "Do you have a mental or physical disorder that poses or is likely to pose a threat to the safety or welfare of yourself or others?",
        ("No", "Yes"),
        index=0,
        key="mental_physical_disorder"
    )
    if q2 == "Yes":
        st.text_area("If yes, please explain", key="mental_physical_disorder_details", height=100)

    st.markdown("---")
    q3 = st.radio(
        "Are you or have you ever been a drug abuser or addict?",
        ("No", "Yes"),
        index=0,
        key="drug_abuser"
    )
    if q3 == "Yes":
        st.text_area("If yes, please explain", key="drug_abuser_details", height=100)

    st.markdown("---")
    q4 = st.radio(
        "Have you ever served in the military?",
        ("No", "Yes"),
        index=0,
        key="served_military"
    )
    if q4 == "Yes":
        st.text_area("If yes, please describe units and dates", key="served_military_details", height=100)

    st.markdown("---")
    q5 = st.radio(
        "Have you ever served in, been a member of, or been involved with a paramilitary unit, vigilante unit, rebel group, guerrilla group, or insurgent organization?",
        ("No", "Yes"),
        index=0,
        key="paramilitary_service"
    )
    if q5 == "Yes":
        st.text_area("If yes, please describe", key="paramilitary_service_details", height=100)
