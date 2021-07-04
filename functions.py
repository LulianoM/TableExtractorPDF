import streamlit as st
import base64
from io import BytesIO



def header_intro():
    col1, col3 = st.beta_columns([1,1])
    with col1:
        st.header('PDF Table Extractor')
        st.text('version 1.0 - Last update 04/07/2022')
    with col3:
        st.image('dados/image1.png', width=150 )
    
def header_intro_2():
    st.write("This application's main functionality is to extract tables from PDF files and generate the download in excel form as quickly and easily as possible.")

def side_bar_credis():
    #Créditos
    st.sidebar.write('Contact:')
    st.sidebar.write('**Luciano Martins Figueira**')
    st.sidebar.write('mailto:contato@lucimartins.com')
    st.sidebar.markdown("[Website](https://www.lucimartins.com/)")
    st.sidebar.markdown("[![GitHub](https://i.stack.imgur.com/tskMh.png) Github](https://github.com/LulianoM)")
    st.sidebar.markdown("[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/martinslucianoufrj/)")
    st.sidebar.image('dados/image3.png', width=250,   )

def downfile(df):
    towrite = BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()  # some strings
    linko = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="pdfextractorbylucimartins.xlsx">Download Excel File</a>'
    st.markdown(linko, unsafe_allow_html=True)