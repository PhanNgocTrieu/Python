# Review:
# Write a function with 3 statements
# Call function

def state():
    print("1")
    print("2")
    print("3")

state()




#############################################################
# function with inputs:
# def my_function(something):
#       Do this with something
#       Then do this
#       Finally do this

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Trieu")


# function with more than 1 input
def gree_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

gree_with("John","Vision 3")
gree_with(location="Nowhere", name="Trieu")
