# import random module
import random

# set the start and end points
random_side = random.randint(0, 1)

# check the conditions
if random_side == 1:
    print(random_side, "- Heads")
else:
    print(random_side, "- Tails")