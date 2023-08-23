import itertools


def main():
    # print 1000 space separated integers starting from 1000 with common difference 500
    # 1000 1500 2000 2500 3000........
    count = 0
    # There should be exactly one space after every integer
    for i in itertools.count(1000, 500):
        if i == 1000*1000:
            break
        else:
            print(i, end = " ")

    #
    # # print all uppercase alphabets 15 times, printing from A-Z then repeating again
    # # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D........
    # # There should be exactly one space after every character
    text = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    text_1 = text.replace(' ','')
    for i in itertools.cycle(text_1):
        if count > 15*26 - 1:
            break
        else:
            print(i, end= ' ')
            count += 1
    #
    # # print list of integers containing 1000 4's
    # print(list(itertools.repeat(1000, 4)))
    print(list(itertools.repeat(1000,4)), end=' ')

    return 0


if __name__ == '__main__':
    main()