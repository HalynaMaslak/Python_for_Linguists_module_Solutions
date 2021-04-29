# -*- coding: utf-8 -*-
"""
Create a program that: Asks for a word; Checks whether it is more frequent
as a Noun or a Verb in the Brown corpus. Display a message if it does not appear
as a noun or a verb in the Brown corpus.
"""
from nltk.corpus import brown
print('The program checks whether the entered word is more frequent as a Noun or a Verb in the Brown corpus.')
word = input('Enter your word: ').lower()
br_words = brown.tagged_words(tagset='universal')
count_N = 0
count_V = 0
for w in br_words:
    if w[0].lower() == word and w[1] == 'NOUN':
        count_N += 1
    elif w[0].lower() == word and w[1] == 'VERB':
        count_V += 1

print('As a Noun:', count_N, 'time(s)')
print('As a Verb:', count_V, 'time(s)')
if count_N > count_V:
    print('Your word', word, 'is more frequent as a Noun.')
elif count_N == count_V !=0:
    print('Your word', word, 'equally appears both as a Noun and a Verb.')
elif count_N < count_V:
    print('Your word', word, 'is more frequent as a Verb.')
elif count_N == 0 and count_V == 0:
    print('Your word', word, 'does not appear as a Noun or a Verb in the Brown corpus.')
