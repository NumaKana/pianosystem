import re

import makefile
import search_phrase

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
    
    col = 0
    rest = []
    score_first = []
    get_rest = search_phrase.search_rest()

    while(col < len(data)): 
        if "\score {" in data[col]:
            break 
        if re.match(".*% 1\\n", data[col]):
            score_first.append(col)
            print("score_first")
            rest.append([col,0])
            count = 1
            s = -1
            while(count > 0):
                if "{" in data[col]: count+=1
                if "}" in data[col]: count-=1
                notes = data[col].split()
                for n, note in enumerate(notes):
                    if re.match('[abcdefgr][eis]*\'*,*\d+', note):
                        print(note)
                        s += 1
                        if s in get_rest:
                            print("rest!!")
                            rest.append([col, n])
                col += 1
        col += 1

    idx_start = rest[m][1]
    idx_end = rest[m+1][1]
    data_end = data[rest[m+1][0]].split()
    data_start = data[rest[m][0]].split()

    data_end_forward = " ".join(data_end[:idx_end])
    data_end_back = " ".join(data_end[idx_end:])
    data_start_forward = " ".join(data_start[:idx_start])
    data_start_back =  " ".join(data_start[idx_start:])

    data[score_first[0]] += change_LightSteelBlue
    data[score_first[1]] += change_LightSteelBlue
    data[rest[m+1][0]] = data_end_forward + change_LightSteelBlue + data_end_back + "\n"
    data[rest[m][0]] = data_start_forward + change_Black + data_start_back + "\n"

    with open("phrase/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("phrase")