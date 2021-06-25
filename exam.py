# -*- coding: utf-8 -*-
"""
Write a programme that:
(a) asks the user to enter a word and identifies all its occurrences in the Brown
corpus where it is used as a noun. Display its frequency as a noun. 10 points

(b) If the word appears in the Brown corpus as a noun, finds which adjective appears
the most often immediately before the given noun. Display how many times this adjective
appears immediately before the noun. 10 points

(c) Using similar processing as in (b), take this adjective and find which noun appears
most frequently after this adjective in the Brown corpus. 20 points

(d) Expand the code from point (b and c) to retrieve the N most frequent adjectives
before the given noun and for each of these adjectives display the most frequent noun
that follows it. N is an integer that the user enters 20 points

If you solve all four points, you do not need to have a different code for (b, c) and (d).
If the code works correctly, (b and c) is a special case of (d) where N = 1.
Make sure you explain how your code works by providing comments.
"""
# import nltk and the Brown corpus
import nltk
from nltk.corpus import brown

user_word = input('Enter a word: ').lower()
number = int(input('How many adjectives to show? Enter a number: '))
# Universal tagset with words and their parts of speech
br_words = brown.tagged_words(tagset='universal')
count_N = 0
# for each word in the Brown corpus: if the words is the same as the user word and is a noun, increment the count
for w in br_words:
    if w[0].lower() == user_word and w[1] == 'NOUN':
        count_N += 1

# let's define a function for tasks b) and c)
def search_bigrams(search_word, quantity, tag):
    freqs = {}
    # for each two words (word and tag) as a bigram: 
    for (w1,t1), (w2,t2) in nltk.bigrams(br_words):
        if tag == 'ADJ':
            if t1 == 'ADJ' and  w2 == search_word and 'NOUN' in t2:
                bigram = ((w1,t1), (w2,t2))
                # update the dictionary count: the bigram and its count as key:value
                freqs[bigram] = freqs.get(bigram,0) + 1
        if tag == 'NOUN':
            if t1 == 'ADJ' and  w1 == search_word and 'NOUN' in t2:
                bigram = ((w1,t1), (w2,t2))
                freqs[bigram] = freqs.get(bigram,0) + 1
    # let's sort the result by the count and take the number of bigrams according to quantity       
    freq = sorted(list(freqs.items()),key=lambda x: x[1],reverse=True)
    return freq[0:quantity]

print(user_word, 'appears', count_N, 'times as a noun.', '\n')
# let's use the function and find user-specified 'number' of the most frequent adjectives before the given noun
b = search_bigrams(user_word, number, 'ADJ')
print('Adjectives that appear before:', user_word, [(a[1],a[0][0][0]) for a in b],'\n')
for adj in b:
    # for all the adjectives lets search the most frequent noun.
    fr_adj = adj[0][0][0]
    c = search_bigrams(fr_adj, 1, 'NOUN')
    print('The most frequent noun that follows the adjective', fr_adj, 'is', c[0][0][1][0], 'with frequency:', str(c[0][1]))


    
        

