'''
Extract list of words from the .csv file. Only take into account words that do not include an invalid character
weird accents, words in two parts..
Save the frequency of each word in a corpus of film subtitles. The corpus can be found at this address:
http://www.lexique.org/telLexique.php
We also save the grammatical category.
'''


import pandas as pd

folder='/path_to_/charabia/data/extracted/lexicon/'
file = 'Lexique382.csv'
df = pd.read_csv(folder + file)

words = df['1_ortho']
freq_film = df['9_freqfilms2']
c_gram = df['4_cgram']

id_valid = []
characters = []
invalid_char = [str(0), str(1), '.', 'ã', 'ñ', ' ']
for w_id in range(len(words)):
    valid=True
    for ch in invalid_char:
        if ch in str(words[w_id]):
            valid=False
    if valid:
        id_valid.append(w_id)
        for c in str(words[w_id]):
            if str(c) not in characters:
                characters.append(str(c))

characters.append(' ')
with open(folder+'lexicon_characters.txt', 'w') as f:
    for w in characters:
        f.write("%s\n" % w)

with open(folder+'lexicon_valid_words_id.txt', 'w') as f:
    for w in id_valid:
        f.write("%s\n" % w)

with open(folder+'lexicon_words.txt', 'w') as f:
    for w in words[id_valid]:
        f.write("%s\n" % w)

with open(folder+'lexicon_freq_film.txt', 'w') as f:
    for w in freq_film[id_valid]:
        f.write("%s\n" % w)

with open(folder+'lexicon_c_gram.txt', 'w') as f:
    for w in c_gram[id_valid]:
        f.write("%s\n" % w)