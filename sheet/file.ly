\version "2.22.2"
% automatically converted by musicxml2ly from sheet/file.mxl
\pointAndClickOff

\header {
    copyright =  "Copyright � 2010 by Bernd Krueger"
    encodingsoftware =  "MuseScore 3.6.2"
    encodingdate =  "2022-12-12"
    title =  SONATINE
    composer =  "M. Clementi OP.36,No.1"
    }

#(set-global-staff-size 20.0)
\paper {
    
    paper-width = 21.01\cm
    paper-height = 29.69\cm
    top-margin = 1.5\cm
    bottom-margin = 1.5\cm
    left-margin = 1.5\cm
    right-margin = 1.51\cm
    indent = 1.6161538461538463\cm
    short-indent = 0.1405351170568562\cm
    }
\layout {
    \context { \Score
        autoBeaming = ##f
        }
    }
PartPOneVoiceOne =  \relative c'' {
    \repeat volta 2 {
        \repeat volta 2 {
            \clef "treble" \numericTimeSignature\time 4/4 \key c \major
            | % 1
            \stemDown c4 ( \stemDown e8 [ \stemDown c8 ] \stemUp g4 ) -.
            \stemUp g4 -. | % 2
            \stemDown c4 ( \stemDown e8 [ \stemDown c8 ] \stemUp g4 ) -.
            \stemDown g'4 -. | % 3
            \stemDown f8 ( [ \stemDown e8 \stemDown d8 \stemDown c8 ]
            \stemDown b8 [ \stemDown c8 \stemDown b8 \stemDown c8 ] | % 4
            \stemDown d8 [ \stemDown c8 \stemDown b8 \stemDown a8 ]
            \stemUp g4 ) r4 \break | % 5
            \stemDown c4 ( \stemDown e8 [ \stemDown c8 ] \stemUp g4 ) -.
            \stemUp g4 -. | % 6
            \stemDown e'4 ( \stemDown g8 [ \stemDown e8 ] \stemDown c4 )
            \stemDown e8 ( [ \stemDown c8 ] | % 7
            \stemDown d8 [ \stemDown b8 \stemDown c8 \stemDown a8 ]
            \stemUp b8 [ \stemUp g8 \stemUp a8 \stemUp fis8 ) ] | % 8
            \stemUp g8 ( [ \stemUp a8 \stemUp b8 \stemUp c8 ] \stemDown
            d8 [ \stemDown e8 \stemDown fis8 \stemDown g8 ) ] \break | % 9
            \stemUp a,4 ( \stemDown a'4 ) \stemDown a4 \stemDown a4 |
            \barNumberCheck #10
            \stemDown b,8 ( [ \stemDown c8 \stemDown d8 \stemDown e8 ]
            \stemDown fis8 [ \stemDown g8 \stemDown a8 \stemDown b8 ) ]
            | % 11
            \stemDown c,4 ( \stemDown c'4 ) \stemDown c4 \stemDown c4 | % 12
            \stemDown d,8 ( [ \stemDown g8 \stemDown b8 \stemDown d8 ]
            \stemDown c8 [ \stemDown b8 \stemDown a8 \stemDown g8 ]
            \break | % 13
            \stemDown fis8 [ \stemDown e8 \stemDown g8 \stemDown fis8 ]
            \stemDown a8 [ \stemDown g8 \stemDown fis8 \stemDown e8 ] | % 14
            \stemDown e8 [ \stemDown d8 \stemDown c8 \stemDown b8 ]
            \stemDown d8 [ \stemDown c8 \stemDown b8 \stemDown a8 ] | % 15
            \stemUp g2 ) r2 }
        \break | % 16
        \stemDown b4 ( \stemDown d8 [ \stemDown b8 ] \stemUp g4 ) -.
        \stemUp g4 -. | % 17
        \stemDown c4 ( \stemDown es8 [ \stemDown c8 ] \stemUp g4 ) -.
        \stemDown g'4 ( | % 18
        \stemDown f4 \stemDown d4 \stemDown es4 \stemDown c4 | % 19
        \stemDown b8 [ \stemDown c8 \stemDown d8 \stemDown b8 ] \stemUp
        g4 ) -. \stemUp g4 -. \break | \barNumberCheck #20
        \stemDown g'8 ( [ \stemDown g,8 \stemDown g'8 \stemDown g,8 ]
        \stemDown g'8 [ \stemDown g,8 \stemDown g'8 \stemDown g,8 ] | % 21
        \stemDown g'8 [ \stemDown g,8 \stemDown g'8 \stemDown g,8 ]
        \stemDown g'8 [ \stemDown g,8 \stemDown g'8 \stemDown g,8 ] | % 22
        \stemDown d'8 [ \stemDown es8 \stemDown f8 \stemDown d8 ]
        \stemDown f8 [ \stemDown es8 \stemDown d8 \stemDown c8 ] | % 23
        \stemDown <b g'>4 ) r4 r2 \pageBreak | % 24
        \stemUp c,4 ( \stemUp e8 [ \stemUp c8 ] \stemUp g4 ) -. \stemUp
        g4 -. | % 25
        \stemUp c4 ( -. \stemUp e8 -. [ \stemUp c8 -. ] \stemUp g4 )
        \stemUp g'4 -. | % 26
        \stemUp f8 ( [ \stemUp e8 \stemUp d8 \stemUp c8 ] \stemUp b8 [
        \stemUp c8 \stemUp b8 \stemUp c8 ] | % 27
        \stemUp d8 [ \stemUp c8 \stemUp b8 \stemUp a8 ] \stemUp g4 ) r4
        \break | % 28
        \stemUp c4 ( \stemUp g8 [ \stemUp c8 ] \stemUp e4 ) -. \stemUp e4
        -. | % 29
        \stemUp e4 ( \stemUp c8 [ \stemUp e8 ] \stemUp g4 ) \stemDown c4
        | \barNumberCheck #30
        \stemUp <e, g>4 -. \stemUp <d f>4 -. \stemUp <c e>4 -. \stemUp
        <b d>4 -. | % 31
        \stemUp c8 ( [ \stemUp d8 \stemUp e8 \stemUp f8 ] \stemUp g8 [
        \stemUp a8 \stemUp b8 \stemUp c8 ) ] \break | % 32
        \stemUp d,4 ( \stemDown d'4 ) \stemDown d4 \stemDown d4 | % 33
        \stemUp e,8 ( [ \stemUp f8 \stemUp g8 \stemUp a8 ] \stemDown b8
        [ \stemDown c8 \stemDown d8 \stemDown e8 ) ] | % 34
        \stemUp f,4 ( \stemDown f'4 ) \stemDown f4 \stemDown f4 \break | % 35
        \stemDown g,8 ( [ \stemDown c8 \stemDown e8 \stemDown g8 ]
        \stemDown f8 [ \stemDown e8 \stemDown d8 \stemDown c8 ] | % 36
        \stemDown a'8 [ \stemDown g8 \stemDown f8 \stemDown e8 ]
        \stemDown d8 [ \stemDown c8 \stemDown b8 \stemDown a8 ] | % 37
        \stemUp g8 [ \stemUp a8 \stemUp f8 \stemUp g8 ] \stemUp e8 [
        \stemUp f8 \stemUp d8 \stemUp e8 ] | % 38
        \stemUp c2 ) r2 }
    }

PartPOneVoiceFive =  \relative c {
    \repeat volta 2 {
        \repeat volta 2 {
            \clef "bass" \numericTimeSignature\time 4/4 \key c \major | % 1
            \stemUp c4 r4 r2 | % 2
            \stemUp c4 r4 r2 | % 3
            \stemUp c4 r4 \stemUp c4 r4 | % 4
            \stemUp g4 r4 \stemDown g'8 ( [ \stemDown f8 \stemDown e8
            \stemDown d8 ] \break | % 5
            \stemUp c4 ) r4 r2 | % 6
            \stemDown c'4 r4 r4 \stemDown fis,4 | % 7
            \stemDown g4 \stemUp c,4 \stemDown d4 \stemUp d,4 | % 8
            \stemUp g4 r4 r2 \break | % 9
            \stemDown fis'8 ( [ \stemDown d'8 \stemDown a8 \stemDown d8
            ] \stemDown fis,8 [ \stemDown d'8 \stemDown a8 \stemDown d8
            ] | \barNumberCheck #10
            \stemDown g,4 ) r4 r2 | % 11
            \stemDown a8 ( [ \stemDown d8 \stemDown c8 \stemDown d8 ]
            \stemDown a8 [ \stemDown d8 \stemDown c8 \stemDown d8 ] | % 12
            \stemDown b4 ) r4 r2 \break | % 13
            \stemDown c4 r4 \stemUp c,4 r4 | % 14
            \stemDown d4 r4 \stemUp d,4 r4 | % 15
            \stemUp g8 ( [ \stemUp b8 \stemUp d8 \stemUp g8 ] \stemUp g,4
            ) r4 }
        \break | % 16
        f''1 ( | % 17
        es1 ) | % 18
        \stemDown b2 \stemDown c2 | % 19
        \stemDown g2 r2 \break | \barNumberCheck #20
        \stemDown f'4 ( \stemDown g,4 \stemDown d'4 \stemDown g,4 | % 21
        \stemDown es'4 \stemDown g,4 \stemDown c4 \stemDown g4 | % 22
        \stemDown b4 ) r4 \stemDown c4 r4 | % 23
        \stemDown g4 \stemUp g,4 \stemDown g'8 ( [ \stemDown f8
        \stemDown e8 \stemDown d8 ] \pageBreak | % 24
        \stemUp c4 ) r4 r2 | % 25
        \stemUp c4 r4 r2 | % 26
        \stemUp c4 r4 \stemUp c4 r4 | % 27
        \stemUp g4 r4 \stemUp g8 ( [ \stemUp f8 \stemUp e8 \stemUp d8 ]
        \break | % 28
        \stemUp c4 ) r4 r2 | % 29
        \stemUp c'4 r4 r2 | \barNumberCheck #30
        \stemDown g'4 r4 \stemUp g,4 r4 | % 31
        \stemUp c4 r4 r2 \break | % 32
        \stemDown b8 ( [ \stemDown g'8 \stemDown d8 -. \stemDown g8 ]
        \stemDown b,8 [ \stemDown g'8 \stemDown d8 \stemDown g8 ] | % 33
        \stemUp c,4 ) r4 r2 | % 34
        \stemDown d8 ( [ \stemDown g8 \stemDown f8 \stemDown g8 ]
        \stemDown d8 [ \stemDown g8 \stemDown f8 \stemDown g8 ] \break | % 35
        \stemDown e4 ) r4 r2 | % 36
        \stemDown f4 r4 \stemDown f4 r4 | % 37
        \stemDown g4 r4 \stemUp g,4 r4 | % 38
        \stemUp c,8 ( [ \stemUp e8 \stemUp g8 \stemUp c8 ] \stemUp c,4 )
        r4 }
    }


% The score definition
\score {
    <<
        
        \new PianoStaff
        <<
            \set PianoStaff.instrumentName = "ピアノ, Clementi: Sonatine Opus 36 Nr. 1, 1. Satz"
            \set PianoStaff.shortInstrumentName = "Pno."
            
            \context Staff = "1" << 
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneVoiceOne" {  \PartPOneVoiceOne }
                >> \context Staff = "2" <<
                \mergeDifferentlyDottedOn\mergeDifferentlyHeadedOn
                \context Voice = "PartPOneVoiceFive" {  \PartPOneVoiceFive }
                >>
            >>
        
        >>
    \layout {}
    % To create MIDI output, uncomment the following line:
    %  \midi {\tempo 4 = 100 }
    }

