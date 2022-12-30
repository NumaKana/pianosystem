#!/bin/bash

echo "lilypond Executed"

chmod -R 777 'LilyPond'
chmod -R 777 'cmd'

"LilyPond/usr/bin/lilypond.exe" --output=sheet -dgui=t --png $1

echo "lilypond Completed"