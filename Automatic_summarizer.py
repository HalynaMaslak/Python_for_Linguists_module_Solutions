# -*- coding: utf-8 -*-
"""
1 Write an automatic summariser based on word frequencies. Do the following steps:
a) Read the contents of a file and split it into sentences and each sentence into tokens.
If you want you can hard code the name of the file in your program or you can ask the user to enter it.
b) Calculate the frequency of each token, ignoring stopwords.
c) Calculate the score of each sentence by adding the scores of the tokens it contains
and normalise it by the number of tokens in the sentence.
d) Extract the n sentences (n specified by the user) with the highest scores and present them
in the order they occur in the text.
"""

import nltk
import nltk.data
from nltk.tokenize import sent_tokenize
# try to open the file. If it can't be open, show an error
try:
    with open('week8_text.txt', 'r', encoding='utf-8') as in_file:
        lines = in_file.readlines()
        
except IOError:
    print("An error occured while opening the file for reading")
# download the tokenizer for German and split the text into sentences
sent_tokenizer=nltk.data.load('tokenizers/punkt/german.pickle')
sents = sent_tokenizer.tokenize(' '.join(lines).replace('\n', ' '))
#print(sents)
# for each sentence in the tockenized text
sent_and_score = {}
for s in sents:
    words_token = nltk.word_tokenize(s)
    #print(words_token)
    # content words are the words excluding punctuation or stopwords in German
    content_words = [word 
         for word in words_token
         if word.isalpha()
         if word.lower() not in nltk.corpus.stopwords.words('german')
        ]
    # total words are the words in the sentence without punctuation
    total_words = [word
                   for word in words_token
                   if word.isalnum()
                   ]
    count_content_words = len(content_words)
    count_total_words = len(total_words)
    sent_score = count_content_words / count_total_words
    #print(sent_score)
    sent_and_score[s] = sent_score
#print(sent_and_score)
   
n_sent = int(input('How many sentences with the highest score should be displayed? '))
cut = sorted(sent_and_score.values(), reverse=True)[n_sent - 1]
count = 0
for i in sent_and_score:
    if sent_and_score[i] >= cut:
        print(i, '\nThe sentence score is: ', sent_and_score[i], '\n')
        count += 1
        if count == n_sent:
            break



