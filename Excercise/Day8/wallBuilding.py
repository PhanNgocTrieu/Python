# Area Calculation
#   You are painting a wall. The instructions on the paint can says that 
#   1 can of paint can cover 5 square meters of wall. Given a random height
#   and width of wall, calculate how many cans of paint you'll need to buy
#   
# Input:    number of can = (wall_height x wall_width) + coverage_per_can
# Output:   How many 

import rano_dom
import math

def canCalculation(weight, height, coverage):
    return math.ceil((weight * height) / coverage)

_weight = rano_dom.randint(1,10)
_height = rano_dom.randint(1,10)
_Coverage = 5


print("Number of Cans:", canCalculation(_weight, _height, _Coverage))

