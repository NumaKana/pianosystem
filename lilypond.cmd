@echo off

echo "lilypond Executed"

chcp 65001

".\LilyPond\usr\bin\lilypond.exe" --output=sheet --png %1

echo "lilypond Completed"