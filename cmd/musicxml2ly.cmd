@echo off

echo "musicxml2ly Executed"

python ".\Lilypond\usr\bin\musicxml2ly.py" --output=sheet/file %1

echo "musicxml2ly Completed"