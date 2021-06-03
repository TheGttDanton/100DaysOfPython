def add(num1, num2):
  return num1 + num2

def divide(num1, num2):
  return num1 / num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

continue_calculation = True

num1 = int(input("Enter the first number \n"))

while continue_calculation:
  num2 = int(input("Enter the second number \n"))
  for symbol in operations:
    print(symbol)
  operation = input("Choose from the above \n")
  function = operations[operation]
  num1 = function(num1, num2)
  print(f"the answer is {num1} ")
  next = input("Do you want to continue with the operation y/n \n").lower()
  
  if next == "n":
    continue_calculation = False
