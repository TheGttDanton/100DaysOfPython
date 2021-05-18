height = float(input("Enter you height in m \n"))
weight = float(input("Enter you weight in kg \n"))

bmi = weight / height ** 2
bmi = round(bmi)

body_type = ""

if bmi < 18.5:
  body_type = "underweight"
elif bmi < 25:
  body_type = "normal weight"
elif bmi < 30:
  body_type = "overweight"
elif bmi < 35:
  body_type = "obese"
else:
  body_type = "clinically obese"

print(f"Your BMI is {bmi} annd you are {body_type}")


