import streamlit as st
import os

num=2
uploaded_files = st.sidebar.file_uploader("upload .mxl file")
col= st.columns(num)
n=0

def makesvg(file): #できない！！
    #make_svg.cmdからコマンドを実行する
    cmd_file = "make_svg.cmd"   # .cmdファイルへのパス
    command = cmd_file + file
    #command += " " + "sheet/file.xml" #ここをupload_fileにしたい
    os.system(command)
    

def show():
    for i in list(range(0,num,1)):
        with col[i]:
            st.image("sheet/file-page"+str(i+n+1)+".png", use_column_width=True)

def main():
    global n
    st.set_page_config(layout="wide")
    if st.sidebar.button("show"): show()

    if st.button("left"): 
        if n > 0: n -= 1
        show()
    if st.button("right"): 
        if n < num: n += 1
        show()
        
    

if __name__ == "__main__":
    main()