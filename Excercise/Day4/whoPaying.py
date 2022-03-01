import rano_dom

test_seed = int(input("Create a seed number: "))
rano_dom.seed(test_seed)


# Split string method
namsAsCSV = input("Give me everybody's names: ")
names = namsAsCSV.split(', ')

print(names)