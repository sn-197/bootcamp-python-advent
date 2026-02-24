# Roll 'em please...
# Tumbling Dice

# use random.randint() to simulate rolling six-sided dice
import random
def roll_die_1():
    return random.randint(1, 6) 
def roll_die_2():
    return random.randint(1, 6)

# roll the dice and print the results
die_1 = roll_die_1()
die_2 = roll_die_2()
print("Die 1:", die_1)
print("Die 2:", die_2)