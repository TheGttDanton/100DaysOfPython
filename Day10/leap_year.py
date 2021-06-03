def is_leap_year(year):
  if year % 100 == 0:
    if year % 400 == 0:
      return True
  elif year % 4 == 0:
    return True
  return False


def days_in_month(year, month):
  months_days = [31,28,31,30,31,30,31,31,30,31,30,31]
  days = months_days[month - 1]
  if month == 2:
    if is_leap_year(year):
      return days + 1
  return days


year = int(input("Enter a year: \n"))
month = int(input("Enter a month: \n"))

days = days_in_month(year, month)

print(f"days in the month is {days}")
