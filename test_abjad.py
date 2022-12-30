import abjad

file = "sheet/file.ly"
data_list = []
with open(file, encoding="utf-8")as f:
    data = f.readlines()
    for d in f:
        data_list.append(d.split())
    
i=0
j=0
clef = ""
preamble = ""
string = " ".join(data[36:107])

while(i < len(data)):
    while(j < len(data[i])):
        if "PartPOneVoiceOne" in data[i]:
            preamble = " ".join(data[:i])
        if "\\clef" in data[i][j]:
            clef = data[i][j+1]
        j+=1
    i+=1

parser = abjad.parser.LilyPondParser()
string = (" ").join(data)
staff = parser(string)
abjad.show(staff)  

#voice = abjad.Voice(string, name="Violin_Voice")
#staff = abjad.Staff([voice], name="Violin_Staff")
#score = abjad.Score([staff], name="Score")
#lilypond_file = abjad.LilyPondFile([score])

#lilypond_file = abjad.LilyPondFile([preamble, score])

#abjad.show(lilypond_file)