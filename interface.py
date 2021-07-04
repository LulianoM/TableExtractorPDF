from os import read
import streamlit as st
import pandas as pd
from tabula import read_pdf
import functions as f

f.header_intro()
f.side_bar_credis()
f.header_intro_2()


st.subheader('Upload your PDF by clicking on "Browse Files"')
input_buffer = st.file_uploader("Upload a file", type=("PDF"))
input_loaded = False

if input_buffer:
    try:
        input_loaded = read_pdf(input_buffer, pages='all')
        st.write(f' - {len(input_loaded)} tables were found in your PDF.')
        T = True
    except Exception as e:
        st.text("Error {}".format(e))

if input_loaded:
    list_ = list(range(0,len(input_loaded)))
    In1 = st.selectbox('Select which table you want to view and download:', list_)
    st.dataframe(input_loaded[In1])
    f.downfile(input_loaded[In1])
