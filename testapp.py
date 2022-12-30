#実行時は py -3.10 -m streamlit run testapp.py

import streamlit as st
import os
import abjad

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


#make_svg.cmdからコマンドを実行する
cmd_file = "make_svg.cmd"   # .cmdファイルへのパス
command = cmd_file

#command += " " + "sheet/file.xml" #ここをupload_fileにしたい


#os.system(command)

if st.button("left"):
    if n > 0: n -= 1

if st.button("right"):
    n += 1

#画像表示
num=2
col=[]
col= st.columns(num)

file = "sheet/file.ly"
with open(file, encoding="utf-8")as f:
    data = f.readlines()

    i=0
    preamble = " ".join(data[:28])
    string = " ".join(data[36:107])

    while(i > len(data)):
        


voice = abjad.Voice(string, name="Violin_Voice")
staff = abjad.Staff([voice], name="Violin_Staff")
score = abjad.Score([staff], name="Score")
lilypond_file = abjad.LilyPondFile([score])

lilypond_file = abjad.LilyPondFile([preamble, score])

abjad.show(lilypond_file)

#for i in list(range(0,num,1)):
#    with col[i]:
#        st.image("sheet/file-page"+str(i+n+1)+".png", use_column_width=True)





