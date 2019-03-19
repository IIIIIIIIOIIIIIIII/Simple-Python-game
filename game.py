'''
stone -> scissors
scissors -> paper
paper -> stone

stone = 0
scissors = 1
paper = 2
'''

import random

L = ['paper', 'stone', 'scissors']

Player = 0
Computer = 0

print('Hello!')

while True:

    element = input('Type element or check score: ')
    if element == 'paper' or element == 'scissors' or element == 'stone':
        var = random.choice(L)
    if element == 'stone' and var == 'scissors':
        print('Computer is ' + var, 'You win!', sep='\n')
        Player += 1
    elif element == 'stone' and var == 'paper':
        print('Computer is ' + var, 'You loose!', sep='\n')
        Computer +=1
    elif element == 'stone' and var == 'stone':
        print('Computer is ' + var, 'Try again!', sep='\n')
        
    elif element == 'scissors' and var == 'scissors':
        print('Computer is ' + var, 'Try again!', sep='\n')
    elif element == 'scissors' and var == 'stone':
        print('Computer is ' + var, 'You loose!', sep='\n')
        Computer +=1
    elif element == 'scissors' and var == 'paper':
        print('Computer is ' + var, 'You win!', sep='\n')
        Player += 1

    elif element == 'paper' and var == 'scissors':
        print('Computer is ' + var, 'You loose!', sep='\n')
        Computer +=1
    elif element == 'paper' and var == 'stone':
        print('Computer is ' + var, 'You win!', sep='\n')
        Player += 1
    elif element == 'paper' and var == 'paper':
        print('Computer is ' + var, 'Try again!', sep='\n')

    elif element == 'score':
        print('Player: ' + str(Player), 'Computer: ' + str(Computer), sep='\n')
    elif element == 'stop': break

    
    
