import re

def makearray():
    file_name = "file/file.ly"

    #ファイルをリストで読み込み
    with open(file_name, encoding="utf-8") as f:
        data = f.read()
        tmp = re.findall(' [a-z][is]*\'*\d+ ', data)
        array = []
        for s in tmp:
            array.append(str.strip(s))
        print(array)


