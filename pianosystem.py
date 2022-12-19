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
show_crip = col_button[1].button("crip")

col_page = st.sidebar.columns(2)
page_back = col_page[0].button("＜")
page_next = col_page[1].button("＞")

reset = st.button("reset")

def init():
    if 'filename' not in st.session_state:
        st.session_state["filename"] = ""
    if 'n' not in st.session_state:
        st.session_state["n"] = 0
    if 'm' not in st.session_state:
        st.session_state["m"] = 0
    if 'cripimg' not in st.session_state:
        st.session_state["cripimg"]  = st.empty()
    if uploaded_files:
        makesvg(file)
        crip(st.session_state["m"])
    

def makesvg(file): #できない！！
    #make_svg.cmdからコマンドを実行する
    cmd_musicxml2ly = "musicxml2ly.cmd"   # .cmdファイルへのパス
    command = cmd_musicxml2ly  + " " + file
    #command += " " + "sheet/file.xml" #ここをupload_fileにしたい
    os.system(command)
    os.system("lilypond.cmd sheet/file.ly")
    
def crip(m):
    file_name = "sheet/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    back = 0
    start = []
    define = []
    end = 0
    match_first = []
    match_last = []

    new_data = []

    while(i < len(data)):
        if "PartPOneVoice" in data[i]:
            start.append(i) 
        if "\clef" in data[i]:
            define.append(i)
        if "The score definition" in data[i]:
            end = i

        if re.match(".*(%\s|#)"+str(int(m)+1)+"\\n", data[i]):
            match_first.append(i+1)
            j = 0
            while(not re.match(".*(%\s|#)"+str(int(m)+5)+"\\n", data[i])):
                if data[i].endswith("}\n"):
                        if j < 4: back = 4 - j
                        break
                if re.match(".*%\s\d+\\n", data[i]):    
                    j += 1
                i += 1
            match_last.append(i+1)
        i += 1


    st.session_state["m"] -= back

    new_data += data[start[0]]
    new_data += data[define[0]]
    new_data += data[match_first[0]:match_last[0]]
    new_data.append("}\n")
    new_data += data[start[1]]
    new_data += data[define[1]]
    new_data += data[match_first[1]:match_last[1]]
    new_data.append("}\n")
    new_data += (data[end:])

    #元のファイルに書き込み
    with open("sheet/crip_file.ly", mode='w', encoding="utf-8") as f:
        f.writelines(new_data)

    os.system("lilypond.cmd sheet/crip_file.ly")


def show(n):
    for i in list(range(0,num,1)):
        with col_img[i]:
            st.image("sheet/file-page"+str(i+n+1)+".png", use_column_width=True)

def crip_show():
    st.session_state["cripimg"].image("sheet/crip_file.png", use_column_width=True)

def main():
    init()
    if reset:
        st.session_state["filename"] = ""
        st.session_state["n"] = 0
        st.session_state["m"] = 0
        makesvg("sheet/file.mxl")
        crip(st.session_state["m"])

    if show_default:
        st.session_state["cripimg"].empty()
        st.session_state["filename"] = "file"
        show(st.session_state["n"])

    if show_crip:
        st.session_state["filename"] = "crip_file"
        crip_show()

    if st.session_state["filename"] == "file":
        st.session_state.cripimg.empty()
        
    if st.session_state.filename == "crip_file":
        col_crip = st.sidebar.columns(2)
        crip_back = col_crip[0].button("back")
        crip_next = col_crip[1].button("next")
        if crip_next:
            st.session_state["m"] +=4
            crip(st.session_state.m)
            crip_show()
        if crip_back:
            if st.session_state.m > 0: st.session_state.m -=4
            crip(st.session_state.m)
            crip_show()

    if page_next: 
        if st.session_state.n < 0: st.session_state.n += 1
        show(st.session_state.n)
    if page_back:
        if st.session_state.n > 0: st.session_state.n -= 1
        show(st.session_state.n)
        

if __name__ == "__main__":
    main()