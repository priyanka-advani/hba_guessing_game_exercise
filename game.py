"""A number-guessing game."""

# Put your code here
from random import randint

print 'Welcome to the Guessing Game!'
player_name = raw_input("What is your name? ")
random_number = randint(1, 100)

number_of_guesses = 0

while True:
    player_guess = int(raw_input('Guess a number between 1 and 100: '))
    number_of_guesses += 1
    if player_guess != random_number:
        if player_guess > random_number:
            print 'Your guess is too high. Try again.'
        elif player_guess < random_number:
            print 'Your guess is too low. Try again.'
    else:
        print 'Congratulations %s, you guessed the correct number in %d guesses!' % (player_name, number_of_guesses)
        break