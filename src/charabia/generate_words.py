"""
Use the table of statistics computed from compute_stats.py to generate new words drawn from these statistics.
"""
import pickle
import numpy as np

# folder containing extracted statistics
folder = 'path_to_/charabia/data/extracted/lexicon/'
# folder in which to save the list of new words
folder_new_words = 'path_to_/charabia/new_words/'
new_words_id = 1
nb_new_words = 1000
length_seq = 3


# load data
characters = []
with open(folder + 'lexicon_characters.txt', 'r') as f:
    for line in f:
        characters.append(line[:-1])
characters.sort()

with open(folder+'lexicon_weighted_count_seq'+str(length_seq)+'.pk', 'rb') as f:
    weighted_counts = pickle.load(f)

length_seq = weighted_counts.ndim

new_words = []
n_nw = 0
while n_nw < nb_new_words: # while we don't have all our new words
    word = ' '*(length_seq-1)
    previous = [0] * (length_seq-1) # list of previous characters
    indices = [0] * (length_seq-1) # list of indices corresponding to the previous characters
    while True: # while word is not finished
        for i in range(length_seq-1):
            previous[i] = word[-(length_seq-(i+1))]
            indices[i] = characters.index(previous[i])
        probas = weighted_counts[tuple(indices)] / weighted_counts[tuple(indices)].sum()

        i_0 = np.random.choice(range(len(characters)), 1, p=probas)[0]

        if characters[i_0] ==  ' ': # word has ended
            break
        word += characters[i_0]
    new_words.append(word[length_seq-1:])
    print(str(n_nw)+'th word created: '+word[length_seq-1:])
    n_nw += 1

new_words_per_size = [[] for i in range(100)]
for w in new_words:
    new_words_per_size[len(w)-1].append(w)

for i in range(16):
    if len(new_words_per_size[i])>0:
        with open(folder_new_words+'/seq_'+str(length_seq)+'/new_words_seq_'+str(length_seq)+'_len'+str(i+1)+'_id'+str(new_words_id)+'.txt', 'w') as f:
            for w in new_words_per_size[i]:
                f.write("%s\n" % w)