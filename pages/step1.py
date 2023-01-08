import streamlit as st

import tools
import makefile
import fourmeasure 

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)

num=2


def main():
    col1, col2 = st.columns(num)
    col_img = [col1, col2]

    col_page = st.sidebar.columns(2)
    page_back = col_page[0].button("＜")
    page_next = col_page[1].button("＞")  

    col_color = st.sidebar.columns(2)
    color_back = col_color[0].button("back")
    color_next = col_color[1].button("next")

    reset = st.button("reset")


    tools.init("4measure")

    if reset:
        tools.reset("4measure")
        fourmeasure.addcolor(st.session_state.m)
    
    if not color_next and not color_back and not page_next and not page_back:
        tools.show("4measure", col_img, st.session_state.n)
        st.stop()
        
    if color_next:
        st.session_state.m +=1
        fourmeasure.addcolor(st.session_state.m)
        tools.show("4measure", col_img, st.session_state.n)
    if color_back:
        if st.session_state.m > 0: st.session_state.m -=1
        fourmeasure.addcolor(st.session_state.m)
        tools.show("4measure", col_img, st.session_state.n)

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        tools.show("4measure", col_img, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        tools.show("4measure", col_img, st.session_state.n)
        
    


if __name__ == "__main__":
    main()