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
    
    i = 0
    start = []
    end = []
    s_start, s_end = search_phrase.search()
    print(s_end)
    while(i < len(data)): 
        if "\score {" in data[i]:
            break     
        if "\clef" in data[i]:
            data.insert(i+1, change_LightSteelBlue)  
        if re.match("Part.*", data[i]):
            data.insert(i+1, change_LightSteelBlue)
            count = 1
            i += 2
            s = 0
            while(count > 0):
                print(s)
                if "{" in data[i]: count += 1
                if "}" in data[i]: count -= 1
                s += len(re.findall('[a-g][is]*\'*,*\d+|\(|\)|\[|\]|-\.', data[i]))
                if s >= s_start[m]:
                    s -= len(re.findall('[a-g][is]*\'*,*\d+|\(|\)|\[|\]|-\.', data[i]))
                    j = 0
                    while(j < len(data[i])):
                        if re.match('[a-g][is]*\'*,*\d+|\(|\)|\[|\]|-\.',data[i][j]): s += 1
                        if s == s_start[m]:
                            start.append([i, j])
                        if s == s_end[m]:
                            end.append([i, j])
                        j+=1
                if s == s_end[m]:
                    end.append([i, j])
                i+=1
        i+=1
    
    print(end)

    idx_start = start[m][1]
    idx_end = end[m][1]
    data[end[m][0]] = data[end[m][0]][:idx_end] + ' ' + change_LightSteelBlue + ' ' + data[end[m][0]][idx_end:]
    data[start[m][0]] = data[start[m][0]][:idx_start] + ' ' + change_Black + ' ' + data[start[m][0]][idx_start:]

    with open("phrase/file.ly", mode='w+', encoding="utf-8") as f:
        f.writelines(data)

    makefile.make_png("phrase")