import streamlit as st

def exibir():
    st.subheader("Upload de Foto")
    st.info("Envie uma foto no formato JPG conforme as especificações do visto.")
    photo = st.file_uploader(
        label="Upload de Foto (JPG)",
        type=["jpg", "jpeg"],
        key="upload_photo"
    )
    if photo:
        st.image(photo, caption="Pré-visualização da foto", use_column_width=True)
