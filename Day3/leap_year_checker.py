year = int(input("Enter the year you want to check \n"))

is_leap_year = False

if year % 100 == 0:
  if year % 400 == 0:
    is_leap_year = True
  else:
    is_leap_year = False
elif year % 4 == 0:
  is_leap_year = True
  
if is_leap_year:
  print("Leap year")
else:
  print("Not Leap year")
