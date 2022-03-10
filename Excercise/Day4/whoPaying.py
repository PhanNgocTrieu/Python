import rano_dom

test_seed = int(input("Create a seed number: "))
rano_dom.seed(test_seed)


# Split string method
namsAsCSV = input("Give me everybody's names: ")
names = namsAsCSV.split(', ')

print(names)

# getting the numbers of persons
nums_people = len(names)

# Generate random person for paying form 0 to the last index
randomPerson = rano_dom.randint(0, nums_people - 1)

print("Person who pays is: ", names[randomPerson])


# Shorter way:
person_who_will_pay = rano_dom.choice(names)
print(person_who_will_pay + " will pay the bill!")