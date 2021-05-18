current_age = input("Enter your cuurent age \n")
current_age = int(current_age)

years_left = 90 - current_age
month_left = 12 * years_left
week_left = 52 * years_left
days_left = 365 * years_left

print(f"you have {days_left} days, {week_left} weeks and {month_left} months")

