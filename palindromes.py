# loading dictionary

'''Loading the txt file as list

Arguments:
    -text files name

Exceptions
    - IOError if filename not found

Returns
    -A list of words in the text file in lower case

'''

import sys

def load(file):
    '''Open the file and return list in lowercase strings'''
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
        return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening {file}. Terminating program', file = sys.stderr)
        sys.exit(1)

word_list = load('dictwords.txt')

'''finding the palindromes in dictionary txt'''
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f'\nNumber of palindromes found : {len(pali_list)}')
print(*pali_list, sep = '\n') #printingeach item on new line, deafult separator






