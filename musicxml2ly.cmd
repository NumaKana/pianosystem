@echo off

echo "musicxml2ly Executed"

py -3.7-32 ".\Lilypond\usr\bin\musicxml2ly.py" --output=sheet/file %1

echo "musicxml2ly Completed"