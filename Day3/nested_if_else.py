print("Welcome to the rollercoaster! \n")
height = int(input("What is your height in cm? \n"))
age = int(input("Enter your age in years \n"))

if height >= 120:
  print("You can ride the rollercoaster!")
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $12")
else:
  print("you cannot ride the rollercoaster!")
