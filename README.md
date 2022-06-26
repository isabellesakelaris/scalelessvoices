# scalelessvoices
A Python program that reads vowel sounds from a text and assigns them musical pitches based on a study by D.C. Miller in Henry Lanz's book, The Physical Basis of Rime, Stanford University, California: Stanford University Press, 1931.

# Artistic freedoms exercised
- For the vowel formants "ih" and "uh," I've assigned G and C respectively, where Miller has not assigned a frequency. I did this to keep all the notes within the same key signature, B Major.
- I've also adjusted all the pitches to exist in the same octave.
- Rather than adding rests between lines or stanzas, I've added them where I felt caesurae in reading the text on my own, usually near the blank space, such as in the third line of the penultimate stanza.

# Future Improvements
- Incorporate vowel formants not captured in Miller's chart 
- Incorporate rhythm based on stressed and unstressed syllabels

# Acknowledgements
I am indebted to a great number of people who helped bring this project to life. My brother, Bennet Sakelaris, encouraged me to begin learning Python and has provided me with much needed troubleshooting tips and moral support along the way. Thank you, Bennet, for your confidence. Additionally, my friend and colleague Jon Allured took the time to meet with me to map out the format and functions I could use to make my first draft of code more efficient. I have learned so much from his generosity and expertise. Thank you, Jon. To my friends who lent me their voices: Jacob and Thomas, I am so grateful for your enthusiasm and willingness to participate in bringing this idea to life. Your support means the world to me.

In this program, I use code and resources developed by Allison Parrish, who created Pronouncing (version 0.2.0), David Kastrup, Werner Lemberg, Han-Wen Nienhuys, Jan Nieuwenhuizen, Carl Sorensen, Janek Warchoł, et al., who created Lilypond (version 2.22.2), the creators of Librosa (Version 0.9.1), Brian Mcfee, Colin Raffel, Dawen Liang, Matt McVicar, Eric Battenberg, and Oriol Nieto, and Ben Welsh, who created and compiled the e.e. cummings free poetry archive. Thank you, all, for sharing your great work.
