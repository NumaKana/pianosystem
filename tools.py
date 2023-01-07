import streamlit as st
import os
import re

def count_file(dir):
    count_file = 0   
    #ディレクトリの中身分ループ
    for file_name in os.listdir(dir): 
        #ファイルもしくはディレクトリのパスを取得
        file_path = os.path.join(dir,file_name)
        #ファイルであるか判定
        if re.match(".*\.png", file_path):
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
        st.session_state.filename = ""

def show(dir, col, n):
    print(dir)
    for i in list(range(0,2,1)):
        with col[i]:
            st.image(dir+"/file-page"+str(i+n+1)+".png", use_column_width=True)