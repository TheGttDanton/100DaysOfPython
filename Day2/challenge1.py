#two_digit_num = int(input("Type any two digit number \n"))

#ones_place = two_digit_num % 10
#tens_place = int(two_digit_num % 100 / 10)

two_digit_num = input("Type any two digit number \n")

ones_place = int(two_digit_num[1])
tens_place = int(two_digit_num[0])


print(ones_place + tens_place)



