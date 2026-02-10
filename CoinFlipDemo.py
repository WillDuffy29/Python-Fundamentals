# Coin Flip Demo

import random

num = random.randint(0, 1)   # Roll a random number that's either 0 or 1

if num > 0.5:                # Number is either 0 or 1. Hence, < 0.5 is 0 and > 0.5 is 1.
  print('Heads')
else:
  print('Tails')