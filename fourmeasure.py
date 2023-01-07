import re
import streamlit as st

import makefile

def addcolor(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    back = 0
    repeat = []
    while(i < len(data)):
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
        if "\clef" in data[i]:
            data.insert(i+1, '\override NoteHead.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Stem.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Beam.color = #(x11-color "LightSteelBlue")\n')
            data.insert(i+1, '\override Accidental.color = #(x11-color "LightSteelBlue")\n')
        if "\\repeat volta" in data[i]:
            repeat.append(i)     
        i+=1

    st.session_state.m -= back

    #元のファイルに書き込み
    with open("4measure/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("4measure")