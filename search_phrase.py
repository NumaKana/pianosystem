import re

def makearray():
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.read()
        array = re.findall('[a-g][is]*\'*,*\d+|\(|\)|\[|\]|-\.', data)
        print(array)
    return array

def search():
    array = makearray()
    a = 0
    start = []
    end = []
    while(a < len(array)):
        if "(" == array[a]: start.append(a)
        if ")" == array[a]: end.append(a)
        a+=1
    return start, end