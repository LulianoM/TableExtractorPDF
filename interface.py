from os import read
import streamlit as st
import pandas as pd
from tabula import read_pdf
from io import BytesIO
import base64


def downfile(df):
    towrite = BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="dadospremigra.xlsx">Download excel file</a>'
    st.markdown(linko, unsafe_allow_html=True)


st.header('Sistema de Extração de PDF - V0.1')
st.text('Atualizado: 2021')

if st.checkbox("Clique ao lado para visulizar o passo a passo de como utilizar o extrator"):
    st.write('Primeiro adicione o arquivo escolhido')

st.subheader('Faça o upload do seu PDF clicando em "Browse Files"')
input_buffer = st.file_uploader("Upload a file", type=("PDF"))
input_loaded = False

if input_buffer:
    try:
        input_loaded = read_pdf(input_buffer, pages='all')
        st.write(f'Há {len(input_loaded)} tabelas em seu PDF')
        T = True
    except Exception as e:
        st.text("Error {}".format(e))

if input_loaded:
    list_ = list(range(0,len(input_loaded)))
    In1 = st.selectbox('Selecione qual tabela deseja visualizar:', list_)
    st.dataframe(input_loaded[In1])
    downfile(input_loaded[In1])
