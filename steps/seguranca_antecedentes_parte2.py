# steps/seguranca_antecedentes_parte2.py
import streamlit as st

def exibir():
    st.header("Security and Background: Part 2")
    st.markdown("Provide complete and accurate answers to all questions that require an explanation.")

    q1 = st.radio(
        "Have you ever been arrested or convicted for any offense or crime, even though subject of a pardon, amnesty, or other similar action?",
        ("No", "Yes"),
        index=0,
        key="arrested_convicted"
    )
    if q1 == "Yes":
        st.text_area("If yes, give details (charges, dates, disposition)", key="arrested_convicted_details", height=100)

    st.markdown("---")
    q2 = st.radio(
        "Have you ever violated, or engaged in a conspiracy to violate, any law relating to controlled substances?",
        ("No", "Yes"),
        index=0,
        key="controlled_substances"
    )
    if q2 == "Yes":
        st.text_area("If yes, please explain", key="controlled_substances_details", height=100)

    st.markdown("---")
    q3 = st.radio(
        "Are you coming to the United States to engage in prostitution or unlawful commercialized vice or have you been engaged in prostitution or procuring prostitutes within the past 10 years?",
        ("No", "Yes"),
        index=0,
        key="prostitution_vice"
    )
    if q3 == "Yes":
        st.text_area("If yes, please explain", key="prostitution_vice_details", height=100)

    st.markdown("---")
    q4 = st.radio(
        "Have you ever been involved in, or do you seek to engage in, money laundering?",
        ("No", "Yes"),
        index=0,
        key="money_laundering"
    )
    if q4 == "Yes":
        st.text_area("If yes, please explain", key="money_laundering_details", height=100)
