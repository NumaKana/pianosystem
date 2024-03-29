import streamlit as st
import os
import re
from datetime import datetime

import makefile

def count_file(dir):
    count_file = 0   
    #ディレクトリの中身分ループ
    for file_name in os.listdir(dir): 
        #ファイルもしくはディレクトリのパスを取得
        file_path = os.path.join(dir,file_name)
        #ファイルであるか判定
        if re.match(".*png", file_path):
            count_file +=1
    print(count_file)
    return count_file


def init(dir):
    if 'n' not in st.session_state:
        st.session_state.n = 0
    if 'm' not in st.session_state:
        st.session_state.m = 0
    if 'l' not in st.session_state:
        st.session_state.l = 0
    if 'filename' not in st.session_state:
        st.session_state.filename = dir
    if 'date' not in st.session_state:
        now = datetime.now()
        st.session_state.date = now.strftime("%Y%m%d%H%M%S")
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = False
    st.session_state.filename = dir


def reset(dir):
    st.session_state.n = 0
    st.session_state.m = 0
    st.session_state.l = 0
    st.session_state.filename = dir


def show(dir, col, n):
    pages = count_file(dir)
    if pages > 1:
        for i in list(range(0,2,1)):
            image = dir+"/file-page"+str(i+n+1)+".png"
            with col[i]:
                st.image(image)
    else:
        st.image(dir+"/file.png")