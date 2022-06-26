pip install pronouncing
import pronouncing
import csv
import pandas as pd
my_csv = pd.read_csv('poems.csv')
poem_texts = my_csv.text 
poem_titles = my_csv.title
poem_books = my_csv.book_title
bee = "IY" #bee
hit = "IH" #hit
they = "EY" #they
pet = "EH" #pet
at = "AE" #at
father = "AO" #father
law = "AA" #law
no = "OW" #no
gloom = "UW" #gloom
pull = "AH" #pull
text = str(poem_texts[0])
text = text.replace('            ', ' \nr2\n')
text = text.replace('    ', ' \nr4\n')
lines = text.split("\n")
word_list = text.split()
stresses = []
phones = []
for word in word_list:
    stresses_list = pronouncing.stresses_for_word(word)
    stresses.append(stresses_list)
    phones_list = pronouncing.phones_for_word(word)
    phones.append(phones_list)
    if word == "r2":
        phones.append(["r2"])
    if word == "r4":
        phones.append(["r4"])

final_phones = []
for phone in phones:
    if (len(phone)) > 1:
        final_phones.append(phone[0])
    else:
        final_phones.append(phone)
        
stress_final = []
for stress in stresses:
    if len(stress) > 1:
        stress_final.append(stress[0])
    else: 
        stress_final.append(stress)
notes = []
equiv_phones = []
for phone in final_phones:
    if bee in phone:
        notes.append("g") 
        equiv_phones.append(phone)
    if hit in phone:
        notes.append("gis")
        equiv_phones.append(phone)    
    if they in phone:
        notes.append("dis")
        equiv_phones.append(phone)    
    if pet in phone:
        notes.append("b")
        equiv_phones.append(phone)   
    if at in phone:
        notes.append("ais")
        equiv_phones.append(phone)
    if father in phone:
        notes.append("des")
        equiv_phones.append(phone)
    if law in phone:
        notes.append("ges")
        equiv_phones.append(phone)
    if no in phone: 
        notes.append("ais")
        equiv_phones.append(phone)
    if pull in phone: 
        notes.append("cis")
        equiv_phones.append(phone)
    if gloom in phone:
        notes.append("g")
        equiv_phones.append(phone)
    if "r2" in phone:
        notes.append("r")
        equiv_phones.append("2")
    if "r4" in phone:
        notes.append("r")
        equiv_phones.append("4")
    
durations = []
for equiv in equiv_phones:
    if "2" in equiv:
        durations.append("2")
    else:
        durations.append("4")
    

zipped = zip(notes, durations)
lilypond_file = open("automated_"+poem_titles[0]+".ly", 'w+')
header = '\\version "2.22.2" \n{\n\\relative\n\\time 2/4\n\\clef "treble"\n'
lilypond_file.write(header)
for the_zip in zipped:
    lilypond_file.write(the_zip[0] + the_zip[1] + '\n')
lilypond_file.write("}")
lilypond_file.close()
