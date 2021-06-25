# -*- coding: utf-8 -*-
"""Week 3. 
Task 3. (For over 80%) Write a program which determines the plural form for an English noun.
Make sure you comment the code and explain how your program works."""

print('Enter a countable noun in singular. The program will show you the plural form of this noun.\nDo not enter proper names, uncountable nouns or words that are not nouns.')
noun = input('ENTER THE NOUN: ').lower()
# this is a list of exceptions: a list of tuples
irreg = [('foot', 'feet'), ('tooth', 'teeth'), ('goose', 'geese'), ('man', 'men'), ('woman', 'women'),
        ('mouse', 'mice'), ('die', 'dice'), ('ox', 'oxen'), ('child', 'children'), ('person', 'people'),
        ('penny', 'pence'), ('louse', 'lice'), ('fez', 'fezzes'), ('gas', 'gasses'), ('knife', 'knives'),
        ('wife', 'wives'), ('life', 'lives'), ('leaf', 'leaves'), ('calf', 'calves'), ('elf', 'elves'), ('loaf', 'loaves'),
        ('photo', 'photos'), ('piano', 'pianos'), ('halo', 'halos'), ('zero', 'zeros'), ('cello', 'cellos'),
        ('phenomenon', 'phenomena'), ('criterion', 'criteria'),
        ('index', 'indices'), ('appendix', 'appendices'), ('vortex', 'vortices')]
# this is a list of nouns that don't change their form in plural
same = ['sheep', 'fish', 'deer', 'moose', 'swine', 'buffalo', 'shrimp', 'trout',
        'aircraft', 'watercraft', 'spacecraft',
        'series', 'species', 'means']
# this is a list of uncountable nouns that end with -s
sing = ['news', 'linguistics', 'athletics', 'darts', 'billiards']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']
#let's check if the entered noun can be found in the list of exceptions. if yes, let's print the plural form of this noun.
exc = ''
for s,pl in irreg:
    if noun not in s: continue
    else:
        exc = noun
        print(pl)
    break

#if the noun is not an exception, let's check other conditions  
if noun != exc:
    if noun in sing:
        print('This noun is always singular')
    elif noun in same:
        print(noun)
    # nouns with an -is ending can be made plural by changing -is to -es.
    elif noun.endswith('is'):
        stem = noun[:-2]
        print(stem, 'es', sep='')
    # words ending in -um shed their -um and replace it with -a to form a plural.
    elif noun.endswith('um'):
        stem = noun[:-2]
        print(stem, 'a', sep='')
    # words of Latin and Greek origin ending in -us change to -i in plural
    elif noun.endswith('us') and len(noun)>3:
        stem = noun[:-2]
        print(stem, 'i', sep='')
    # if the singular noun ends in ‑s, -ss, -sh, -ch, -x, or -z, add ‑es to the end to make it plural
    elif noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z', 'o')):
        print(noun, 'es', sep='')
    # if a singular noun ends in ‑y and the letter before the -y is a consonant, we change the ending to ‑ies
    elif noun.endswith('y') and noun[-2] in consonants:
        stem = noun[:-1]
        print(stem, 'ies', sep='')
    else:
        print(noun, 's', sep='')
