import streamlit as st

import makefile
import tools

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)
    

def main():
    num=2
    col_img= st.columns(num)

    col_page = st.sidebar.columns(2)
    page_back = col_page[0].button("＜")
    page_next = col_page[1].button("＞")

    pages = tools.count_file("file")

    tools.init("file")
    if st.button("reset"):
        tools.reset("file")
        makefile.make_png("file")
        pages = tools.count_file("file")
    
    if not page_next and not page_back:
        makefile.make_png("file")
        tools.show("file", col_img, st.session_state.n)
        st.stop()

    if page_next: 
        if st.session_state.n < pages-1: st.session_state.n += 2
        tools.show("file", col_img, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 2
        tools.show("file", col_img, st.session_state.n)
        
    


if __name__ == "__main__":
    main()