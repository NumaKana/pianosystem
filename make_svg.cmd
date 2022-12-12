@echo off

echo ".cmd Executed"

REM[ py -3.7-32 ".\Lilypond\usr\bin\musicxml2ly.py" --output=sheet/file ]

".\LilyPond\usr\bin\lilypond.exe" --output=sheet --png "sheet/file.ly"

echo "Completed"