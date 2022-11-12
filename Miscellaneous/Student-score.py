student_scores = input("Input a list of student score:").split()
for n in range(0, len(student_scores)):
    student_scores[n] =  int(student_scores[n])
print(student_scores)

highest_score = 0

for i in  student_scores:
    if highest_score < i:
        highest_score = i

print(highest_score)