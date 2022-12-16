import streamlit as st
import os
import re

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)

num=2
col_img= st.columns(num)
file = "sheet/file.mxl"

uploaded_files = st.sidebar.file_uploader("upload .mxl file")

col_button = st.sidebar.columns(2)
show_default = col_button[0].button("default")
show_color = col_button[1].button("4小節ずつ")

col_page = st.sidebar.columns(2)
page_back = col_page[0].button("＜")
page_next = col_page[1].button("＞")

def init():
    if st.button("reset"):
        st.session_state.n = 0
        st.session_state.m = 0
        makesvg("sheet/file.mxl")
        addcolor(st.session_state.m)
    if uploaded_files:
        makesvg(file)
        addcolor()
    if 'filename' not in st.session_state:
        st.session_state.filename = ""
    if 'n' not in st.session_state:
        st.session_state.n = 0
    if 'm' not in st.session_state:
        st.session_state.m = 0
    

def makesvg(file): #できない！！
    #make_svg.cmdからコマンドを実行する
    cmd_musicxml2ly = "musicxml2ly.cmd"   # .cmdファイルへのパス
    command = cmd_musicxml2ly  + " " + file
    #command += " " + "sheet/file.xml" #ここをupload_fileにしたい
    os.system(command)
    os.system("lilypond.cmd sheet/file.ly")
    
def addcolor(m):
    file_name = "sheet/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    back = 0
    repeat = []
    while(i < len(data)):
        if "\\repeat volta" in data[i]:
            repeat.append(i)     

        if re.match(".*(%\s|#)"+str(int(m)+1)+"\\n", data[i]):
            data.insert(i+1, '\override NoteHead.color = #(x11-color "red")\n')
            data.insert(i+1, '\override Stem.color = #red\n')
            data.insert(i+1, '\override Beam.color = #red\n')
            j=0
            while(not re.match(".*(%\s|#)"+str(int(m)+5)+"\\n", data[i])):
                if data[i].endswith("}\n"):
                    if repeat:
                        if j < 4: back = 4 - j
                        break
                if re.match(".*%\s\d+\\n", data[i]):    
                    j+=1
                i+=1
            data.insert(i+1, '\override NoteHead.color = #(x11-color "black")\n')
            data.insert(i+1, '\override Stem.color = #black\n')
            data.insert(i+1, '\override Beam.color = #black\n')
        i+=1

    st.session_state.m -= back
        
    

    #元のファイルに書き込み
    with open("sheet/alt_file.ly", mode='w', encoding="utf-8") as f:
        f.writelines(data)

    os.system("lilypond.cmd sheet/alt_file.ly")


def show(filename, n):
    for i in list(range(0,num,1)):
        with col_img[i]:
            st.image("sheet/"+filename+"-page"+str(i+n+1)+".png", use_column_width=True)

def main():
    init()
    if show_default:
        st.session_state.filename = "file"
        show(st.session_state.filename, st.session_state.n)
    if show_color:
        st.session_state.filename = "alt_file"
        show(st.session_state.filename, st.session_state.n)
        
    if st.session_state.filename == "alt_file":
        col_color = st.sidebar.columns(2)
        color_back = col_color[0].button("back")
        color_next = col_color[1].button("next")
        if color_next:
            st.session_state.m +=4
            addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)
        if color_back:
            if st.session_state.m > 0: st.session_state.m -=4
            addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        show(st.session_state.filename, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        show(st.session_state.filename, st.session_state.n)
        
    


if __name__ == "__main__":
    main()