import rano_dom 

test_seed = int(input("Create a seed number: "))
rano_dom.seed(test_seed)

random_size = rano_dom.randint(0,1)

if random_size == 1:
    print("Heads")
else:
    print("Tails")