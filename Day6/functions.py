def my_function():
  print("Hello")
  print("Bye")

counter = 0
while counter < 4:
  print(f"Calling for {counter} time")
  my_function()
  counter += 1

