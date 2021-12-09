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


anagram_list = []
# input a single word or single name below to find its anagram
name = input('Enter word for conversion :')   #foster
print(f"Input name = {name}")
name = name.lower()
print(f'Using name = {name}')

# sort names and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

        # priting out the list of anagrams

print()
if len(anagram_list) == 0:
    print('Damn! No anagrams found. You need larger dictionary bruh')
else:
    print(f"Anagrams: {anagram_list}", sep= '\n')