# scalelessvoices
A Python program that reads vowel sounds from a text and assigns them musical pitches based on a study by D.C. Miller in Henry Lanz's book, The Physical Basis of Rime, Stanford University, California: Stanford University Press, 1931.

Artistic freedoms exercised:
- For the vowel formants "ih" and "uh," I've assigned G and C respectively, where Miller has not assigned a frequency. I did this to keep all the notes within the same key signature, B Major.
- I've also adjusted all the pitches to exist in the same octave.
- Rather than adding rests between lines or stanzas, I've added them where I felt caesurae in reading the text on my own, usually near the blank space, such as in the third line of the penultimate stanza.


Future Improvements:
- Incorporate consonants and vowels not captured in Miller's chart 
- Incorporate rhythm based on stressed and unstressed syllabels
- Automate rests
- Automate creation of lilypond file
