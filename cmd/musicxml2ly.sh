#!/bin/bash
@echo off

echo "musicxml2ly Executed"

chmod -R 777 'LilyPond'
chmod -R 777 'cmd'

"LilyPond/usr/bin/musicxml2ly.py" --output=sheet/file %1

echo "musicxml2ly Completed"