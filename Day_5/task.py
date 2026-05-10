student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max = student_scores[0]

for i in range(1, len(student_scores) - 1):
    if student_scores[i] > max:
        max = student_scores[i]


print(max)

# Gauss challenge
# Work out the total numbers between 1 and 100, inclusive of both 1 and 100

sum = 0

for i in range(1, 101):
    sum += i

print(sum)