import streamlit as st

import makefile
import tools

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)

num=2
col_img= st.columns(num)

col_page = st.sidebar.columns(2)
page_back = col_page[0].button("＜")
page_next = col_page[1].button("＞")
    

def main():
    tools.init("file")
    tools.show("file", col_img, st.session_state.n)
    if st.button("reset"):
        st.session_state.n = 0
        st.session_state.m = 0
        st.session_state.l = 0
        st.session_state.filename = "file"
        makefile.makesvg("file")

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        tools.show("file", col_img, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        tools.show("file", col_img, st.session_state.n)
        
    


if __name__ == "__main__":
    main()