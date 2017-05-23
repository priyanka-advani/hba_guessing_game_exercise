"""A number-guessing game."""

# Put your code here
from random import randint

print 'Welcome to the Guessing Game!'
player_name = raw_input("What is your name? ")
random_number = randint(1, 100)
