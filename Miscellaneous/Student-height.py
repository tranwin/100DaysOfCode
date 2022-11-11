student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Find the total
sum_height = 0
for i in student_heights:
    sum_height += i
print (sum_height)

#Find the number
number_of_student = 0
for i in student_heights:
    number_of_student += 1
print (number_of_student)

print(sum_height/number_of_student)


