"""
Compute Markov statistics from corpus. Sequences of length length_seq are considered. length_seq -1 characters are added
at the beginning and one at the end of each word (so that each character has length_seq characters before it).
We compute the probabilities of each combination of length_seq characters.
The counts then converted to probabilities can be weighted by the words frequencies in a movie subtitles corpus.
"""

import numpy as np
import pickle

length_seq = 3
folder = 'path_to_/charabia/data/extracted/lexicon/'
weight_by_freq = False

# load data
characters = []
with open(folder + 'lexicon_characters.txt', 'r') as f:
    for line in f:
        characters.append(line[:-1])
characters.sort()

words = []
with open(folder + 'lexicon_words.txt', 'r') as f:
    for line in f:
        words.append(line[:-1])

freq_film = []
with open(folder + 'lexicon_freq_film.txt', 'r') as f:
    for line in f:
        freq_film.append(float(line[:-1]))

freq_film = np.array(freq_film)
nb_char = len(characters)

# counts of sequences frequences
# dimension i represents length_seq-(i+1)th characters preceding the current (therefore the last dimension is the current character).
dim_table = [nb_char]*length_seq
weighted_counts = np.zeros(dim_table)

for i, w in enumerate(words):
    # add length_seq-1 spaces before and 1 after
    word = ' '*(length_seq-1) + w + ' '
    len_word = len(word)
    for char_index in range(length_seq-1,len_word):
        chars = [] # contains the characters of the sequence up to the current character
        inds = [] # contains the index of these characters in the list of characters
        for j in range(length_seq):
            chars.append(word[char_index-(length_seq-1-j)])
            inds.append(characters.index((chars[j])))
        if weight_by_freq:
            weighted_counts[tuple(inds)] += freq_film[i] # add frequency of the word to each sequence in this word
        else:
            weighted_counts[tuple(inds)] += 1

# save weighted counts
with open(folder+'lexicon_weighted_count_seq'+str(length_seq)+'.pk', 'wb') as f:
    pickle.dump(weighted_counts, f)








