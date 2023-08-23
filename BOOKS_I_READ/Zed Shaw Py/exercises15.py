from sys import argv

'''this is a scripting exercises.
to run this file you will have to go with 
`python3 exercise15.py lyrics.txt` 
giving the argument in terminal before the script even starts. 
This is I believe what they call scripting.'''

script, filename = argv
txt = open(filename)

print(f'Here is your file {filename}: ')
print(txt.read())

print('Type the filename again : ')
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

txt.close()
