

'''
Author; Captain Murlidhar Singh
purpose; Guess The Number Game
Date; 2nd November of 2020 
'''


# Guess The Number Game

m=33
a=input('Enter Your Name/ID_ ')
print('\nGUESS THE NUMBER GAME')
print('\nWelcome', a.capitalize(),'!\n')
print('GAME RULES;\n1.You Have 9 Attempts Only.')
print('2.The Number Should Must Between 11 to 99.\n')
print('TIPS;\n 1. [ > ] = Greater Than\n',
    '2. [ < ] = Less Than\n')
print('Now, Guess The Number', a.capitalize(),"_")
g=1
while(g<=9):
    t=int(input())
    if t>=99 or t<=11:
        print('Read The Rules Carefully & Try Again!')
    elif t>=75:
        print('Enter Number < 75')
    elif t>=49:
        print('Enter Number < 49')
    elif t>=40:
        print('Enter Number < 40')
    elif t>=35:
        print('Enter Number < 35')
    elif t<=21:
        print('Enter Number > 21')
    elif t<=31:
        print('Enter Number > 31')
    elif t==m:
        print('Great!, You Guess The Right Number')
        print('Thanks For Coming!\n')
        break
    elif t==32 or 34 :
        print('You Are Almost There!, Enter Number')
    else:
        print('Read The Rules Carefully & Try Again!')
    print(9-g, 'Attempt Left!')
    g=g+1

if g>9:
    print('Game Over!\nThanks For Coming!\n')
