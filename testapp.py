#実行時は py -m streamlit run testapp.py

import streamlit as st
import os

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

os.system(command)

if st.button("left"):
    if n > 0: n -= 1

if st.button("right"):
    n += 1

#画像表示
num=2
col=[]
col= st.columns(num)

for i in list(range(0,num,1)):
    with col[i]:
        st.image("sheet/file-page"+str(i+n+1)+".png", use_column_width=True)





