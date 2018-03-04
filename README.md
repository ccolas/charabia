# charabia
Generator of invented words from a corpus statistics

Based on the idea developped in this french blog post: https://sciencetonnante.wordpress.com/2015/10/16/la-machine-a-inventer-des-mots-video/

This code extract words and word frequencies from a french corpus of books and movie subtitles (available here: http://www.lexique.org/telLexique.php)

Using this corpus, it computes statistics of character sequences (whose length can be changed as a parameter).
New words are then generated following these statistics.

Adaptation to other languages should not be too hard. The part of the code computing statistics and generating new words only requires:
- a list of words as .txt, one per line
- a list of characters as .txt, ' ' being included
- a list of frequencies for each word (optional)

Weighting the statistics by the frequency of the words does not seem to produce positive effects.
Indeed, words with weird sequences of characters tend to be quite frequent. For instance, 'cinq' and 'coq' in french are two
frequent words using 'q' at the end of the word and there are probably the only words following this rule. Weighting by the
frequency would give a lot of importance to the sequence 'q' + end of the word, which would look weird in any invented word.

Author: Cédric Colas
Email: cdric.colas@gmail.com
