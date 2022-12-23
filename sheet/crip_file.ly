PartPOneVoiceOne =  \relative c'' {
            \clef "treble" \numericTimeSignature\time 4/4 \key c \major
            \stemDown c4 ( \stemDown e8 [ \stemDown c8 ] \stemUp g4 ) -.
            \stemUp g4 -. | % 6
            \stemDown e'4 ( \stemDown g8 [ \stemDown e8 ] \stemDown c4 )
            \stemDown e8 ( [ \stemDown c8 ] | % 7
            \stemDown d8 [ \stemDown b8 \stemDown c8 \stemDown a8 ]
            \stemUp b8 [ \stemUp g8 \stemUp a8 \stemUp fis8 ) ] | % 8
            \stemUp g8 ( [ \stemUp a8 \stemUp b8 \stemUp c8 ] \stemDown
            d8 [ \stemDown e8 \stemDown fis8 \stemDown g8 ) ] \break | % 9
}
PartPOneVoiceFive =  \relative c {
            \clef "bass" \numericTimeSignature\time 4/4 \key c \major | % 1
            \stemUp c4 ) r4 r2 | % 6
            \stemDown c'4 r4 r4 \stemDown fis,4 | % 7
            \stemDown g4 \stemUp c,4 \stemDown d4 \stemUp d,4 | % 8
            \stemUp g4 r4 r2 \break | % 9
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

