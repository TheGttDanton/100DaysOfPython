total_bill = input("What was the total bill ? \n")
percent_tip = input("What percentage tip would you like to give? \n")
total_person = input("How many people to split the bill? \n")

total_bill = float(total_bill)
percent_tip = float(percent_tip)
total_person = int(total_person)

total_pay = total_bill * ( 1 + percent_tip / 100)
each_person_share = total_pay / total_person
each_person_share = round(each_person_share, 2)

print(f"Each person should pay ${each_person_share}")
