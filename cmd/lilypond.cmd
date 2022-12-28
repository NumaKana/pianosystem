@echo off

echo "lilypond Executed"

chcp 65001

call "cmd/lilypond.exe" --output=sheet -dgui=t --png %1

echo "lilypond Completed"