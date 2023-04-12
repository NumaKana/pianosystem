import re

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

def getphrase(m):
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
    
    i = 0
    start = []
    end = []
    while(i < len(data)): 
        if "\score {" in data[i]:
            break     
        if "\clef" in data[i]:
            data.insert(i+1, change_LightSteelBlue)  
        if re.match("Part.*", data[i]):
            data.insert(i+1, change_LightSteelBlue)
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

    data[end[m]] = data[end[m]][:idx_end] + ' ' + change_LightSteelBlue + ' ' + data[end[m]][idx_end:]
    data[start[m]] = data[start[m]][:idx_start] + ' ' + change_Black + ' ' + data[start[m]][idx_start:]

    with open("phrase/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("phrase")
