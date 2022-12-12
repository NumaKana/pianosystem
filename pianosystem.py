import streamlit as st
import os

st.set_page_config(
    page_title="アプリケーション名",
    layout="wide",
    initial_sidebar_state="expanded"
)


num=2
i=0 
file = "sheet/file.xml"

uploaded_files = st.sidebar.file_uploader("upload .mxl file")
col= st.columns(num)

def init():
    if uploaded_files:
        makesvg(file)
        addcolor()
    if 'filename' not in st.session_state:
        st.session_state.filename = ""
    if 'n' not in st.session_state:
        st.session_state.n = 0
    

def makesvg(file): #できない！！
    #make_svg.cmdからコマンドを実行する
    cmd_musicxml2ly = "musicxml2ly.cmd"   # .cmdファイルへのパス
    command = cmd_musicxml2ly  + file
    #command += " " + "sheet/file.xml" #ここをupload_fileにしたい
    os.system(command)
    os.system("lilypond.cmd sheet/file.ly")
    
def addcolor():
    file_name = "sheet/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    data.insert(28, '    \override NoteHead.color = #(x11-color "LimeGreen")\n')

    #元のファイルに書き込み
    with open("sheet/alt_file.ly", mode='w', encoding="utf-8") as f:
        f.writelines(data)

    os.system("lilypond.cmd sheet/alt_file.ly")


def show(filename, n):
    for i in list(range(0,num,1)):
        with col[i]:
            st.image("sheet/"+filename+"-page"+str(i+n+1)+".png", use_column_width=True)

def main():
    init()

    if st.sidebar.button("makesvg"):
        makesvg("")
        
    if st.sidebar.button("default"):
        st.session_state.filename = "file"
        show(st.session_state.filename, st.session_state.n)

    if st.sidebar.button("color"):
        st.session_state.filename = "alt_file"
        show(st.session_state.filename, st.session_state.n)

    if st.button("left"): 
        if st.session_state.n > 0: st.session_state.n -= 1
        show(st.session_state.filename, st.session_state.n)
    if st.button("right"):
        if st.session_state.n < num: st.session_state.n += 1
        show(st.session_state.filename, st.session_state.n)


if __name__ == "__main__":
    main()