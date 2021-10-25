import random

roll = random.randint(1,6)

guess = int(input('Guess the dice role:\n'))

if guess == roll:
    print("Correct! They role a " + str(roll))
else:
    print("Wrong! They role a " + str(roll))