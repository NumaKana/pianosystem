@echo off

echo "lilypond Executed"

chcp 65001

start "cmd/lilypond.exe" --output=sheet -dgui=t --png %1

echo "lilypond Completed"