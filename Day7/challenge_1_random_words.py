import random

word_list = ["ardvark", "baboon", "camel"]

random_choice = random.choice(word_list)

guessed_letter = input("Guess a letter of the word \n").lower()

for letter in random_choice:
  if letter == guessed_letter:
    print("Right")
  else:
    print("Wrong")
