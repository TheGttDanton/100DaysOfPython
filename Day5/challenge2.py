student_scores = input("Input a list of students score, separated by comma").split(",")


for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max = 0

for score in student_scores:
  if score > max:
    max = score

print(f"max score is {max}")
