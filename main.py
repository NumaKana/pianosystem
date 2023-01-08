import streamlit as st

import tools

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)

num=2
col_img= st.columns(num)
file = "sheet/file.mxl"

uploaded_files = st.file_uploader("upload .mxl file")
    

def main():
    tools.init("")



        
    


if __name__ == "__main__":
    main()