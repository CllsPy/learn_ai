import streamlit as st
from summarizer import Summarizer

st.text("")
col1, col2 = st.columns(2)
videoURL = col1.text_input(label="URL do vídeo")

model = st.radio(
    "Selecione um modelo",
    ["mT5", "Pegasus", "BART"])

model = str(model)

if st.button("Enviar"):
    st.write(Summarizer(link=videoURL, model=model))

else:
    st.write("")
    
