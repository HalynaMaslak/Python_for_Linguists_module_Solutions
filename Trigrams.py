# -*- coding: utf-8 -*-
"""
Develop a program that will give you the possibility to search for 
three-word phrases that have a specified sequence of part of speech. Select
the Brown corpus from NLTK and ask the user for the sequence of parts of speech.
Output all the words of the given structure. For the sake of simplicity use the
universal tagset (i.e. brown.tagged_words(tagset='universal') 
"""
import nltk
from nltk.corpus import brown
print('''Choose three parts of speech and the program will look for the specified sequence in the Brown corpus.
The tags are:''')
print('_'*25)
print('''
ADJ adjective
ADP	adposition
ADV	adverb
CONJ conjunction	
DET	determiner, article
NOUN noun
NUM	numeral
PRT	particle
PRON pronoun
VERB verb
. punctuation marks
X other''')
print('_'*25)
POS1 = input('Enter the first part of speech: ')
POS2 = input('Enter the second part of speech: ')
POS3 = input('Enter the third part of speech: ')

br_words = brown.tagged_words(tagset='universal')
examples = []
for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(br_words):
    if t1 == POS1 and t2 == POS2 and t3 == POS3 :
        examples.append(((w1,t1), (w2,t2), (w3,t3)))
# let's unpack the tuple and print 10 examples of the required sequence
for item in examples[:10]:
    print(*item)
        