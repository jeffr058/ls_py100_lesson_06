# The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.

# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.

import random
random_number = random.randint(0, 1)

# My solution
if random_number:   # removed == 1 to leverage truthiness concept
    print('Yes!')
else:               # changed from elif random_number == 0
    print('No.')