# steps/informacoes_endereco_telefone.py

import streamlit as st

def exibir():
    st.header("Endereço e Telefone")
    
    st.subheader("Endereço Residencial")
    st.text_input("Endereço (Linha 1)", key="home_street1")
    st.text_input("Endereço (Linha 2) *Opcional", key="home_street2")
    st.text_input("Cidade", key="home_city")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text_input("Estado/Província", key="home_state")
    with col2:
        st.checkbox("Não se aplica", key="home_state_na")
    col3, col4 = st.columns([3, 1])
    with col3:
        st.text_input("CEP", key="home_zip")
    with col4:
        st.checkbox("Não se aplica", key="home_zip_na")
    st.selectbox(
        "País/Região",
        options=["Selecione...", "Brasil", "Estados Unidos", "Outro"],
        key="home_country"
    )

    st.markdown("---")
    st.subheader("Endereço de Correspondência")
    st.radio(
        "Seu endereço de correspondência é o mesmo que o residencial?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="mail_same"
    )
    if st.session_state.mail_same == "Não":
        st.text_input("Endereço (Linha 1)", key="mail_street1")
        st.text_input("Endereço (Linha 2) *Opcional", key="mail_street2")
        st.text_input("Cidade", key="mail_city")
        col5, col6 = st.columns([3, 1])
        with col5:
            st.text_input("Estado/Província", key="mail_state")
        with col6:
            st.checkbox("Não se aplica", key="mail_state_na")
        col7, col8 = st.columns([3, 1])
        with col7:
            st.text_input("CEP", key="mail_zip")
        with col8:
            st.checkbox("Não se aplica", key="mail_zip_na")
        st.selectbox(
            "País/Região",
            options=["Selecione...", "Brasil", "Estados Unidos", "Outro"],
            key="mail_country"
        )

    st.markdown("---")
    st.subheader("Telefone")
    st.text_input("Número de telefone principal", key="phone_primary")
    st.text_input("Número de telefone secundário *Opcional", key="phone_secondary")
    st.checkbox("Não se aplica", key="phone_secondary_na")
    st.text_input("Número de telefone comercial *Opcional", key="phone_work")
    st.checkbox("Não se aplica", key="phone_work_na")
    st.radio(
        "Você usou outros números de telefone nos últimos cinco anos?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="phone_other_used"
    )
    if st.session_state.phone_other_used == "Sim":
        st.text_input("Número de telefone adicional", key="phone_additional")

    st.markdown("---")
    st.subheader("E-mail")
    st.text_input("Endereço de e-mail", key="email_primary")
    st.radio(
        "Você usou outros endereços de e-mail nos últimos cinco anos?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="email_other_used"
    )
    if st.session_state.email_other_used == "Sim":
        st.text_input("Endereço de e-mail adicional", key="email_additional")

    st.markdown("---")
    st.subheader("Mídias Sociais")
    st.radio(
        "Você tem presença em mídias sociais nos últimos cinco anos?",
        options=["Selecione...", "Sim", "Não"],
        index=0,
        key="social_presence"
    )
    if st.session_state.social_presence == "Sim":
        opcoes_social = [
            "Selecione...",
            "ASK.FM",
            "DOUBAN",
            "FACEBOOK",
            "FLICKR",
            "GOOGLE+",
            "INSTAGRAM",
            "LINKEDIN",
            "MYSPACE",
            "PINTEREST",
            "QZONE (QQ)",
            "REDDIT",
            "SINA WEIBO",
            "TENCENT WEIBO",
            "TUMBLR",
            "TWITTER",
            "TWOO",
            "VINE",
            "Nenhuma"
        ]
        st.selectbox(
            "Plataforma de Mídia Social",
            options=opcoes_social,
            key="social_platform"
        )
        st.text_input("Identificador na plataforma", key="social_identifier")
