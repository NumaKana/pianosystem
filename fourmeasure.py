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

def get_fourmeasure():
    file_name = "file/file.ly"
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = 0
    j = 1
    back = 0
    repeat = []
    count = 0
    start = []
    end = []

    while(i < len(data)):
        if "\score {" in data[i]:
            break
        if "\\repeat volta" in data[i]: repeat.append(i) 
        if re.match(".*(%\s|#)"+str(j)+"\\n", data[i]):
            start.append(j)
            count = 0
            while(count < 4):
                if re.match(".*(%\s|#)\d+\\n", data[i]): count+=1
                if "\\repeat volta" in data[i]: repeat.append(i) 
                if data[i].endswith("}\n"):
                    if repeat: 
                        repeat.pop()
                        break
                i+=1
            end.append(j+count)
            j += count
            i-=1
        i+=1
    return start, end



def addcolor(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()

    i = len(data) - 1
    start, end = get_fourmeasure()
    while(i > 0):
        if re.match(".*(%\s|#)"+str(start[m])+"\\n", data[i]):
            data.insert(i+1, change_Black)
        if re.match(".*(%\s|#)"+str(end[m])+"\\n", data[i]):
            data.insert(i+1, change_LightSteelBlue)
        if "\clef" in data[i]:
            data.insert(i+1, change_LightSteelBlue)  
        i-=1



    #元のファイルに書き込み
    with open("4measure/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("4measure")