student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62
}

students_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    grade = "Outstanding"
  elif score > 80:
    grade = "Exceeds expectations"
  elif score > 70:
    grade = "Acceptable"
  else:
    grade = "Fail"
    
  students_grades[student] = grade


print(students_grades)
