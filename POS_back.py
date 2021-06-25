# -*- coding: utf-8 -*-
"""
1. [Parts of speech] In every natural language, the same word can represent different parts of speech in different contexts.
Consider the ambiguous English word “back”. Provide all possible parts of speech (POS) that this word can have and add
an example sentence for each part of speech. Please use the list of part-of-speech tags from here:
http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html#Word.
"""

import nltk
from nltk.corpus import brown

with open("Grammarly_task1.txt", "w+") as f:
    
    sents = brown.tagged_sents()
    word = 'back'
        
    res = []      
    for s in sents:
        for w in s:
            if w[0].lower() == word:
                res.append((w[1],s))
                            
    res.sort()
    
    for x in res:
        f.write(x[0])
        f.write(' ')
        text = ''
        for pair in x[1]:
            text += pair[0]
            text += ' '
        f.write(text)
        f.write('\n')
        