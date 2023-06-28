import re

def makearray():
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.read()
#        array = re.findall('[a-z][is]*\'*,*\d+|\(|\)|\[|\]|-\.', data)
        array = re.findall('[abcdefgr][eis]*\'*,*\d+', data)  
#        print(array)
    return array

def search_rest():
    array = makearray()
    rest = []
    for a, ar in enumerate(array):
        if re.match("r\d", ar): 
            if len(rest) != 0 and rest[-1] == a-1:
                rest.pop()
            rest.append(a)
    if rest[0] == 0: del rest[0]
    return rest