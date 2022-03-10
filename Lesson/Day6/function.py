# start with function
# to define a function - using def keyword

from calendar import SATURDAY


def sayingHello():
    print("hello")
    print("bye")

# when running withou calling it -> it would not be use
# calling like this below:
sayingHello()


### indentation
# the distance from the first column for knowing that someine inside anothers
# example:
def my_function():
    # This is the first indentation
    if 1:
        # this is the second order of indentation
        sayingHello()
# two ways of making indentation
# 1) Spaces
# 2) Tabs
# Normally we would use tabs 