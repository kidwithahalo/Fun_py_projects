"""
Created on Tue May 24 17:50:45 2022
@author: pankajksingh
"""

from sys import exit

def gold_room():
    print('This room is full of gold. How  much do you take?')  
    
    choice = input('> ')
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead('Man, learn to round off a deal!!')

    if  how_much < 50:
        print('Nice, you are not greedy, you win!')
        exit(0)
    else:
        dead('You greedy bastard')


def bear_room():
    print('There is a bear here')
    print('The bear has a bunch of honey')
    print('The fat bear is in front of another door')
    print('How are you going to move the bear?\ntaunt bear/take honey')
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == 'take honey':
            dead('The bear looks at you and slaps your face off')
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear has moved from the door')
            print('You can go inside now. \nYou do : taunt bear/open door')
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead('The bear gets pissed off and chews your leg off')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print('I have no idea what that means :(')

def cthulhu_room():
    print('Here you see the evil Cthulhu')
    print('He, it, whatever stares at you and you go insane')
    print('Do you flee for your life or eat your head? flee/head ')

    choice = input('> ')
    if 'flee' in choice:
        start()
    elif 'head'  in choice:
        dead('Well, that was tasty!!')
    else:
        cthulhu_room()

def dead(why):
    print(why, ', Good Job!')
    exit(0)

def start():
    print('You are in a dark room')
    print('There is a door to your left and right')
    print('Which one do you pick: left/right')

    choice = input('> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve')

start()
