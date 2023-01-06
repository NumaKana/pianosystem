import streamlit as st
import os
import re
import subprocess

import makefile

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
    
def addcolor(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    back = 0
    repeat = []
    while(i < len(data)):
        if "\clef" in data[i]:
            data.insert(i+1, '\override NoteHead.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Stem.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Beam.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Accidental.color = #(x11-color "LightSteelBlue")\n')
        if "\\repeat volta" in data[i]:
            repeat.append(i)     

        if re.match(".*(%\s|#)"+str(int(m)+1)+"\\n", data[i]):
            data.insert(i+1, '\override NoteHead.color = #(x11-color "black")\n')
            data.insert(i+1, '\override Stem.color = #black\n')
            data.insert(i+1, '\override Beam.color = #black\n')
            data.insert(i+1, '\override Accidental.color = #black\n')
            j=0
            while(not re.match(".*(%\s|#)"+str(int(m)+5)+"\\n", data[i])):
                if data[i].endswith("}\n"):
                    if repeat:
                        if j < 4: back = 4 - j
                        break
                if re.match(".*%\s\d+\\n", data[i]):    
                    j+=1
                i+=1
            data.insert(i+1, '\override NoteHead.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Stem.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Beam.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Accidental.color = #(x11-color "LightSteelBlue")\n')
        i+=1

    st.session_state.m -= back

    #元のファイルに書き込み
    with open("4measure/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("4measure")

def getphrase(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
    
    i = 0
    start = []
    end = []
    while(i < len(data)):      
        if "\clef" in data[i]:
            data.insert(i+1, '\override NoteHead.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Stem.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Beam.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Accidental.color = #(x11-color "LightSteelBlue")\n')   
        if re.match("PartPOneVoiceOne.*", data[i]):
            data.insert(i+1, '\override NoteHead.color = #(x11-color "LightSteelBlue")\n')
            count = 1
            i += 2
            while(count > 0):
                if "{" in data[i]: count += 1
                if "}" in data[i]: count -= 1
                if "(" in data[i]: start.append(i)
                if ")" in data[i]: end.append(i)
                i+=1
        i+=1
    
    idx_start = list(data[start[m]]).index("(") -4
    idx_end = list(data[end[m]]).index(")") + 2
    if len(list(data[end[m]])) > idx_end:
        if list(data[end[m]])[idx_end] == "]": idx_end += 2

    data[end[m]] = data[end[m]][:idx_end] + ' \override NoteHead.color = #(x11-color "LightSteelBlue") ' + data[end[m]][idx_end:]
    data[start[m]] = data[start[m]][:idx_start] + '\override NoteHead.color = #(x11-color "black") ' + data[start[m]][idx_start:]

    with open("phrase/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("phrase")


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
        addcolor(st.session_state.m)
        getphrase(st.session_state.m)

    if st.button("getphrase"):
        st.session_state.n = 0
        st.session_state.m = 0
        st.session_state.l = 0
        getphrase(st.session_state.l)

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
            addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)
        if color_back:
            if st.session_state.m > 3: st.session_state.m -=4
            addcolor(st.session_state.m)
            show(st.session_state.filename, st.session_state.n)

    if st.session_state.filename == "phrase":
        col_phrase = st.sidebar.columns(2)
        phrase_back = col_phrase[0].button("back")
        phrase_next = col_phrase[1].button("next")
        if phrase_next:
            st.session_state.l += 1
            getphrase(st.session_state.l)
            show(st.session_state.filename, st.session_state.n)
        if phrase_back:
            if st.session_state.l > 0: st.session_state.l -= 1
            getphrase(st.session_state.l)
            show(st.session_state.filename, st.session_state.n)

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        show(st.session_state.filename, st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        show(st.session_state.filename, st.session_state.n)
        
    


if __name__ == "__main__":
    main()