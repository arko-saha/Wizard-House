
# import the module

import random

# variables

number_of_guesses = 0

lowerLimit = random.randint(1,1000)
upperLimit = random.randint(lowerLimit,5000)
number = random.randint(lowerLimit,upperLimit)

# inputs 

player_name = input("Hello, What's your name? - ")

print('okay, '+ player_name+ ', I am trying to remember a number between '+ str(lowerLimit) +' and '+ str(upperLimit) +'. Can you help me with that?')

# loop

for number_of_guesses in range(20):
    if number_of_guesses < 20:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low.') 
        elif guess > number:
            print('Your guess is too high.')
        elif guess == number:
            break
    else:
        break
        

# output

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries! ')
    if number_of_guesses < 5:
        print('Welcome to Griffindor!')
    elif number_of_guesses > 5:
        if number_of_guesses < 10:
            print('Welcome to Hufflepuff!')
        elif number_of_guesses > 10:
            if number_of_guesses < 15:
                print('Welcome to Ravenclaw!')
            elif number_of_guesses > 15:
                if number_of_guesses < 20:
                    print('Welcome to Slytherin!')
            
        
else:
    print('You could not guess the number, The number was ' + str(number))
    print('Yeah, not your piece of cake, you dumbass muggle!')
