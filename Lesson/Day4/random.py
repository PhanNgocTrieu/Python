#import lib of random
import rano_dom # error when import random module -> change file name to another one (Except random.py)

# Module:
# How to use module -> import from file
random_int = rano_dom.randint(1,10)
print(random_int)

import random_module

random_module.hello()


# random of floating number
random_float = rano_dom.random() * 5
print(random_float)


love_score = rano_dom.randint(1,100)
print(f"Your love score is {love_score}")