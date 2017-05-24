"""A number-guessing game."""

# Put your code here
from random import randint

print 'Welcome to the Guessing Game!'
player_name = raw_input("What is your name? ")
print 'Hi, %s! I\'m thinking of a number between 1 and 100.' % (player_name)
print 'Try to guess my number.'

random_number = randint(1, 100)

number_of_guesses = 0

while True:
    player_guess = raw_input('What is your guess? ')
    if '.' in player_guess:
        print 'We rounded down your guess to the nearest whole number.'
    try:
        player_guess = int(float(player_guess))
    except ValueError:
        print 'Please enter a valid number.'
        continue

    if player_guess < 1 or player_guess > 100:
        print 'Please enter a number between 1 and 100 '
    else:
        number_of_guesses += 1
        if player_guess != random_number:
            if player_guess > random_number:
                print 'Your guess is too high. Try again.'
            elif player_guess < random_number:
                print 'Your guess is too low. Try again.'
        else:
            print 'Congratulations %s, you guessed the correct number in %d guesses!' % (player_name, number_of_guesses)
            break


try:
    guess_float = float(player_guess) # this checks if player_guess is a number (float or int)
except ValueError:
    print 'enter a valid number'
    continue

# this checks if the string is an integer
if player_guess.isdigit():
    # intify
    player_guess = int(player_guess)
else:
    # rounding down
    player_guess = int(guess_float)
    print 'We rounded down your guess'



# we've got a good int
