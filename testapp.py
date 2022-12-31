#実行時は py -m streamlit run testapp.py

import streamlit as st
import os
import subprocess

n = 0

st.set_page_config(layout="wide")
st.title("title")

#-------
#.xmlファイルを読み込むプログラム sidebarに表示
#まだできてない
uploaded_files = st.sidebar.file_uploader("upload .xml file")

#uploaded_filesは配列
#for uploaded_file in uploaded_files:
#    st.write("filename:", uploaded_file)
#-----

file = "sheet/file.ly"


if st.button("left"):
    if n > 0: n -= 1

if st.button("right"):
    n += 1

#画像表示
num=2
col=[]
col= st.columns(num)

pro = subprocess.Popen("LilyPond\\usr\\bin\\lilypond.exe -h")
pro.poll() == None

#for i in list(range(0,num,1)):
#    with col[i]:
#        st.image(abjad.show(file), use_column_width=True)





