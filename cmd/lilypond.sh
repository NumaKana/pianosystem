#!/bin/bash

echo "lilypond Executed"

chmod -R 777 'LilyPond'
chmod -R 777 'cmd'

"lilypond-2.22.2-1.mingw.exe" --output=sheet -dgui=t --png $1

echo "lilypond Completed"