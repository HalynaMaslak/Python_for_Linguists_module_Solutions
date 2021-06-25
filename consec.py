# -*- coding: utf-8 -*-
"The programme checks the entered word for two consecutive letters."

word = input('Enter your word here to check double letters: ').lower()
prev = ''
double = list()
for l in word:
   if l == prev:
       double.append(l*2)
   prev = l
print('In your word there are such double letters: ', double)