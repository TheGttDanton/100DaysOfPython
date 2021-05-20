student_height = input("Input a list of students heights, separated by comma").split(",")


for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])

counter = 0
total_height = 0
for height in student_height:
  total_height += height
  counter += 1

if total_height == 0:
  print("average height is 0")
else:
  average = total_height / counter
  average = int(average)
  print(f"average height is {average}")
