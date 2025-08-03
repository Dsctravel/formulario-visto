# steps/seguranca_antecedentes_parte3.py

import streamlit as st

def exibir():
    st.subheader("Security and Background: Part 3")

    # 1) Espionagem, sabotagem, etc.
    espionagem = st.radio(
        "Você pretende se envolver em espionagem, sabotagem, violações de controle de exportação ou qualquer outra atividade ilegal nos Estados Unidos?",
        ["Não", "Sim"],
        index=0,
        key="espionagem"
    )
    if espionagem == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_espionagem")

    st.markdown("---")

    # 2) Atividades terroristas
    terrorismo = st.radio(
        "Você pretende se envolver em atividades terroristas nos Estados Unidos ou já participou de atividades terroristas?",
        ["Não", "Sim"],
        index=0,
        key="terrorismo"
    )
    if terrorismo == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_terrorismo")

    st.markdown("---")

    # 3) Apoio financeiro ou outro suporte a terroristas
    apoio = st.radio(
        "Você já forneceu ou pretende fornecer apoio financeiro ou outro suporte a terroristas ou organizações terroristas?",
        ["Não", "Sim"],
        index=0,
        key="apoio_terrorista"
    )
    if apoio == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_apoio")

    st.markdown("---")

    # 4) Membro ou representante de organização terrorista
    membro = st.radio(
        "Você é membro ou representante de uma organização terrorista?",
        ["Não", "Sim"],
        index=0,
        key="membro_terrorista"
    )
    if membro == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_membro")

    st.markdown("---")

    # 5) Dependente beneficiado por atividade terrorista
    dependente = st.radio(
        "Você é cônjuge, filho(a) ou dependente de alguém que participou de atividade terrorista e se beneficiou disso nos últimos cinco anos?",
        ["Não", "Sim"],
        index=0,
        key="dependente_terrorismo"
    )
    if dependente == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_dependente")

    st.markdown("---")

    # 6) Genocídio
    genocidio = st.radio(
        "Você já ordenou, incitou, cometeu, assistiu ou participou de genocídio?",
        ["Não", "Sim"],
        index=0,
        key="genocidio"
    )
    if genocidio == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_genocidio")

    st.markdown("---")

    # 7) Tortura
    tortura = st.radio(
        "Você já ordenou, incitou, cometeu, assistiu ou participou de tortura?",
        ["Não", "Sim"],
        index=0,
        key="tortura"
    )
    if tortura == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_tortura")

    st.markdown("---")

    # 8) Execuções extrajudiciais / violência política
    execucoes = st.radio(
        "Você já cometeu, ordenou, incitou, assistiu ou participou de execuções extrajudiciais, assassinatos políticos ou outros atos de violência?",
        ["Não", "Sim"],
        index=0,
        key="execucoes"
    )
    if execucoes == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_execucoes")

    st.markdown("---")

    # 9) Recrutamento ou uso de crianças-soldados
    criancas = st.radio(
        "Você já recrutou ou utilizou crianças-soldados?",
        ["Não", "Sim"],
        index=0,
        key="criancas_soldados"
    )
    if criancas == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_criancas")

    st.markdown("---")

    # 10) Violações de liberdade religiosa
    oficial = st.radio(
        "Você, enquanto funcionário público, já foi responsável por ou participou de graves violações da liberdade religiosa?",
        ["Não", "Sim"],
        index=0,
        key="oficial_governo"
    )
    if oficial == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_oficial")

    st.markdown("---")

    # 11) Controles populacionais forçados
    controle = st.radio(
        "Você já participou diretamente no estabelecimento ou execução de controles populacionais forçando aborto ou esterilização contra a vontade?",
        ["Não", "Sim"],
        index=0,
        key="controle_populacao"
    )
    if controle == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_controle")

    st.markdown("---")

    # 12) Transplante coercitivo de órgãos ou tecidos
    transplante = st.radio(
        "Você já participou diretamente no transplante coercitivo de órgãos ou tecidos humanos?",
        ["Não", "Sim"],
        index=0,
        key="transplante"
    )
    if transplante == "Sim":
        st.text_area("Se sim, descreva:", key="detalhes_transplante")
