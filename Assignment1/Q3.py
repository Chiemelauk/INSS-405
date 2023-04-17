#choose 17 as the number of courses taken by the user

num_courses = 17
total_score = 0

#create a loop of 17 numbers and calculate the total score:

for i in range(17):
    score = int(input(f"Enter final score for course {i+1}: "))
    total_score += score

#To perform the average
average = total_score / num_courses

#To determine the grades use the if and elif statement:
if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif average >= 75 and average <= 79:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"

#To perform conditional statement for the functions:
print(f"Total score: {total_score}")
print(f"Average score: {average}")
print(f"Grade: {grade}")


