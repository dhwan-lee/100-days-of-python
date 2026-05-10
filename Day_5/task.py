student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max = student_scores[0]

for i in range(1, len(student_scores) - 1):
    if student_scores[i] > max:
        max = student_scores[i]


print(max)