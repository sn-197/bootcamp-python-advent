# Roll 'em Pete... twice, if you please  - https://youtu.be/B4iQnkdVpxw ; - https://www.youtube.com/watch?v=HmRofx_suTg
# Tumbling Dice - Rolling Stones - https://youtu.be/XAWjSTwvroY?list=RDXAWjSTwvroY

# use random.randint() to simulate rolling six-sided dice
import random
def roll_die():
    return random.randint(1, 6) 

# roll the dice and print the results
die_1 = roll_die()
die_2 = roll_die()  # Use roll_die() for the second die
die_3 = roll_die()  # Use roll_die() for the third die
print("Die 1:", die_1)
print("Die 2:", die_2)
print("Die 3:", die_3)