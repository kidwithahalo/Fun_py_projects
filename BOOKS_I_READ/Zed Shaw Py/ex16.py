from sys import argv

script, filename = argv

print(f'We are going to erase {filename}')
print("If you don't want that , hit CTRL-C")
print('If you do want that , press RETURN')

input('? ')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye.')
target.truncate()

print('Now I am going to ask three lines for new file.')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('I am going to write these to the new file:')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally we ar closing the file.')
target.close()