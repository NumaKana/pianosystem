import streamlit as st
import re

import makefile
import phrase
import fourmeasure

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)

num=2
col_img= st.columns(num)
file = "sheet/file.mxl"

uploaded_files = st.sidebar.file_uploader("upload .mxl file")

col_button = st.sidebar.columns(3)
show_default = col_button[0].button("default")
show_color = col_button[1].button("4小節")
show_phrase = col_button[2].button("フレーズ")

col_page = st.sidebar.columns(2)
page_back = col_page[0].button("＜")
page_next = col_page[1].button("＞")

def init():
    if uploaded_files:
        makesvg(file)
    if 'n' not in st.session_state:
        st.session_state.n = 0
    if 'm' not in st.session_state:
        st.session_state.m = 0
    if 'l' not in st.session_state:
        st.session_state.l = 0
    if 'filename' not in st.session_state:
        st.session_state.filename = ""
    

def makesvg(dir): #できない！！
    #make_svg.shからコマンドを実行する
    #command += " " + "sheet/file.xml" #ここをupload_fileにしたい
    makefile.mxl_ly()
    makefile.make_png(dir)

def show(dir, n):
    for i in list(range(0,num,1)):
        with col_img[i]:
            st.image(dir+"/file-page"+str(i+n+1)+".png", use_column_width=True)

def main():
    init()
    if st.button("reset"):
        st.session_state.n = 0
        st.session_state.m = 0
        st.session_state.l = 0
        st.session_state.filename = ""
        makesvg("file")
        fourmeasure.addcolor(st.session_state.m)
        phrase.getphrase(st.session_state.m)

    if st.button("getphrase"):
        st.session_state.n = 0
        st.session_state.m = 0
        st.session_state.l = 0
        phrase.getphrase(st.session_state.l)

    if show_default:
        st.session_state.filename = "file"
        show(st.session_state.filename, st.session_state.n)
    if show_color:
        st.session_state.filename = "4measure"
        show(st.session_state.filename, st.session_state.n)
    if show_phrase:
        st.session_state.filename = "phrase"
        show(st.session_state.filename, st.session_state.n)
        
    if st.session_state.filename == "4measure":
        col_color = st.sidebar.columns(2)
        color_back = col_color[0].button("back")
        color_next = col_color[1].button("next")
        if color_next:
            st.session_state.m +=4
            fourmeasure.addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)
        if color_back:
            if st.session_state.m > 3: st.session_state.m -=4
            phrase.addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)

    if st.session_state.filename == "phrase":
        col_phrase = st.sidebar.columns(2)
        phrase_back = col_phrase[0].button("back")
        phrase_next = col_phrase[1].button("next")
        if phrase_next:
            st.session_state.l += 1
            phrase.getphrase(st.session_state.l)
            show(st.session_state.filename, st.session_state.n)
        if phrase_back:
            if st.session_state.l > 0: st.session_state.l -= 1
            phrase.getphrase(st.session_state.l)
            show(st.session_state.filename, st.session_state.n)

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        show(st.session_state.filename, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        show(st.session_state.filename, st.session_state.n)
        
    


if __name__ == "__main__":
    main()