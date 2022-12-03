@echo off

echo ".cmd Executed"

py -3.7-32 ".\Lilypond\usr\bin\musicxml2ly.py" --output=sheet/file sheet/file.xml

".\LilyPond\usr\bin\lilypond.exe" --output=sheet --png "sheet/file.ly"

echo "Completed"