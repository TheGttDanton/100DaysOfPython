weight = float(input("Enter your weight in kg"))
height = float(input("Enter your height in meter"))

bmi = round(weight / height ** 2, 2)

print("your bmi is: " + str(bmi)) 
