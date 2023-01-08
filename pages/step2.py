import streamlit as st

import tools
import phrase 
import makefile

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

col_color = st.sidebar.columns(2)
color_back = col_color[0].button("back")
color_next = col_color[1].button("next")

def main():
    tools.init("phrase")
    tools.show("phrase", col_img, st.session_state.n)
    if st.button("reset"):
        st.session_state.n = 0
        st.session_state.m = 0
        st.session_state.l = 0
        st.session_state.filename = "phrase"
        makefile.makesvg("phrase")
        phrase.getphrase(st.session_state.m)

    if color_next:
        st.session_state.m +=4
        phrase.getphrase(st.session_state.m)
        tools.show("phrase", col_img, st.session_state.n)
    if color_back:
        if st.session_state.m > 3: st.session_state.m -=4
        phrase.getphrase(st.session_state.m)
        tools.show("phrase", col_img, st.session_state.n)

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        tools.show("phrase", col_img, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        tools.show("phrase", col_img, st.session_state.n)
        
    


if __name__ == "__main__":
    main()