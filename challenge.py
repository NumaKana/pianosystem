import abjad

preamble = r"""\\header {
    copyright =  "Copyright � 2010 by Bernd Krueger"
    encodingsoftware =  "MuseScore 3.6.2"
    encodingdate =  "2022-12-12"
    title =  SONATINE
    composer =  "M. Clementi OP.36,No.1"
    }

\#(set-global-staff-size 20.0)
\\paper {
    
    paper-width = 21.01\\cm
    paper-height = 29.69\\cm
    top-margin = 1.5\\cm
    bottom-margin = 1.5\\cm
    left-margin = 1.5\\cm
    right-margin = 1.51\\cm
    indent = 1.6161538461538463\\cm
    short-indent = 0.1405351170568562\\cm
    }
\\layout {
    \\context { \Score
        autoBeaming = \#\#f
        }
    }"""

repeat = abjad.Repeat(repeat_count=2, repeat_type='volta')
voice = abjad.Voice("c'4 d'4 e'4 f'4", name="PartPOneVoiceOne")
staff = abjad.Staff([voice], name="1")
score = abjad.Score([staff], name="Score")
lilypond_file = abjad.LilyPondFile([score])