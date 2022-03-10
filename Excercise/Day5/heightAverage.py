student_heights = [180, 124, 165, 173, 189, 169, 149]

# input:
numOfStudents = input("Input a number: ").split()
for n in range(0, len(numOfStudents)):
    numOfStudents[n] = int(numOfStudents[n])

average = 0
students = len(numOfStudents)

for height in numOfStudents:
    average += height


print(f"height Average : {average/students}")
print(f"Another way: {sum(numOfStudents)/len(numOfStudents)}")
