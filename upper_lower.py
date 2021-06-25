'''1. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.'''

def count_Up_Low(text):
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    count_upper = 0
    count_lower = 0
    for char in text:
        if char in upper:
            count_upper += 1

        elif char in lower:
            count_lower +=1
    print('Number of upper case letters:', count_upper)
    print('Number of lower case letters', count_lower)
    
txt = input('Enter the text to calculate the number of upper and lower case letters. TEXT: ')
count_Up_Low(txt)
    