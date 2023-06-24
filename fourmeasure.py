import re
import streamlit as st

import makefile

change_LightSteelBlue = """
\override NoteHead.color = #(x11-color "LightSteelBlue")
\override Stem.color = #(x11-color "LightSteelBlue")
\override Beam.color = #(x11-color "LightSteelBlue")
\override Accidental.color = #(x11-color "LightSteelBlue")
\override Slur.color = #(x11-color "LightSteelBlue")
\override Staff.Rest.color = #(x11-color "LightSteelBlue")
\override Staff.LedgerLineSpanner.color = #(x11-color "LightSteelBlue")
"""

change_Black = """
\override NoteHead.color = #(x11-color "Black")
\override Stem.color = #(x11-color "Black")
\override Beam.color = #(x11-color "Black")
\override Accidental.color = #(x11-color "Black")
\override Slur.color = #(x11-color "Black")
\override Staff.Rest.color = #(x11-color "Black")   
\override Staff.LedgerLineSpanner.color = #(x11-color "Black")
"""

def search_break():
    file_name = "file/file.ly"
    array = []
    i = 0

    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
    while(i < len(data)):
        if re.match(".*% 1\\n", data[i]):
           array.append(i)
        if "\\break" in data[i]:
            array.append(i)
        i+=1
    print(array)
    return array

def get_fourmeasure():
    file_name = "file/file.ly"
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    j = 1
    back = 0
    repeat = []
    count = 0
    array = []

    while(i < len(data)):
        if "\score {" in data[i]:
            break
        if "\\repeat " in data[i]: repeat.append(i) 
        if re.match(".*(%\s|#)"+str(j)+"\\n", data[i]):
            array.append(j)
            count = 0
            while(count < 4):
                if re.match(".*(%\s|#)\d+\\n", data[i]): count+=1
                if "\\repeat " in data[i]: repeat.append(i) 
                if data[i].endswith("}\n"):
                    if repeat: 
                        repeat.pop()
                        break
                i+=1
            j += count
            i-=1
        i+=1
    return array



def addcolor(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data_all = f.read()
    with open(file_name, encoding="utf-8") as l:
        data = l.readlines()

    if "\\break" in data_all:
        array = search_break()
        i = len(data) - 1
        while(i > 0):
            if i == array[m]:
                data.insert(i+1, change_Black)
            if i == array[m+1]:
                data.insert(i+1, change_LightSteelBlue)
            if "% 1\n" in data[i]:
                data.insert(i+1, change_LightSteelBlue)  
            i-=1
    else:
        array = get_fourmeasure()
        i = len(data) - 1
        while(i > 0):
            if re.match(".*(%\s|#)"+str(array[m])+"\\n", data[i]):
                data.insert(i+1, change_Black)
            if re.match(".*(%\s|#)"+str(array[m]-1)+"\\n", data[i]):
                data.insert(i+1, change_LightSteelBlue)
            if "% 1\n" in data[i]:
                data.insert(i+1, change_LightSteelBlue)  
            i-=1

    #元のファイルに書き込み
    with open("4measure/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("4measure")