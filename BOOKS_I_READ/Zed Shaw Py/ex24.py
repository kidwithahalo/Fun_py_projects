# this is exercise 25 though

def break_words(stuff):
    '''This functions will break up the words for us'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''sort the words'''
    return sorted(words)
    # its good that we used sorted instead of words.sort() as this
    # creates a whole new file

def print_first_words(words):
    '''print the first words after popping it up'''
    word = words.pop(0)
    print(word)
    print(f'The remaining words are :{words}')

def print_last_word(words):
    '''prints last word'''
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    '''takes a full sentence and returns sorted words'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''prints first and last word fo the sentence'''
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)

