#!/bin/bash

echo "lilypond Executed"

chmod -R a+x 'LilyPond'
"cmd/lilypond.exe" --output=sheet -dgui=t --png $1

echo "lilypond Completed"