def prime_checker(number):
  is_prime_number = False
  for n in range(2, int(number / 2)):
    if number % n == 0:
      is_prime_number = True
      break

  if is_prime_number == False:
    print("Its a prime number")
  else:
    print("Its not a prime number")
    
    
number = int(input("Enter a number: \n" ))
prime_checker(number)
