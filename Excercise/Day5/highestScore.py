numOfStudents = input("Input a number: ").split()
for n in range(0, len(numOfStudents)):
    numOfStudents[n] = int(numOfStudents[n])

highestScore = 0

for student in numOfStudents:
    if student > highestScore:
        highestScore = student

print("The highest scores: ", highestScore)
print("The highest scores: ", max(numOfStudents))
