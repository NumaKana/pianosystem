import streamlit as st

import tools
import phrase 

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

    pages = tools.count_file("file")

    tools.init("phrase")
    phrase.getphrase(st.session_state.l)

    if reset:
        tools.reset("phrase")
        phrase.getphrase(st.session_state.l)
        pages = tools.count_file("file")
    
    if not color_next and not color_back and not page_next and not page_back:
        tools.show("phrase", col_img, st.session_state.n)
        st.stop()
        
    if color_next:
        st.session_state.l +=1
        phrase.getphrase(st.session_state.l)
        tools.show("phrase", col_img, st.session_state.n)
    if color_back:
        if st.session_state.l > 0: st.session_state.l -=1
        phrase.getphrase(st.session_state.l)
        tools.show("phrase", col_img, st.session_state.n)

    if page_next: 
        if st.session_state.n < pages: st.session_state.n += 2
        tools.show("phrase", col_img, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 2
        tools.show("phrase", col_img, st.session_state.n)
        
    


if __name__ == "__main__":
    main()