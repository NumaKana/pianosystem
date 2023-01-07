import re
import streamlit as st

import makefile

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