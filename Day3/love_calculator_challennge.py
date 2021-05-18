print("Welcome to the python love calculator \nn")

name1 = input("What is your name ? \n")
name2 = input("What is his/her name ? \n")

name1 = name1.lower()
name2 = name2.lower()

combined = name1 + name2

true_count = 0
## True score
true_count += combined.count("t")

true_count += combined.count("r")

true_count += combined.count("u")

true_count += combined.count("e")

love_count = 0
## Love score
love_count += combined.count("l")

love_count += combined.count("o")

love_count += combined.count("v")

love_count += combined.count("e")


score = true_count * 10 + love_count

if score < 10 or score > 90:
  print(f"Your score is {score} and you are like coke and mentoes")

elif score > 40 and score < 50:
  print(f"Your score is {score} and you are alright together")

else:
  print(f"Your score is {score}")



