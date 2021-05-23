import random

word_list = ["ardvark", "baboon", "camel"]

random_choice = random.choice(word_list)

guessed_word = ["_"] * len(random_choice)

print(f"the word chosen is {random_choice}")
print(f"{guessed_word}")

guessed_letter = input("Guess a letter of the word \n").lower()

for (index, letter) in enumerate(random_choice):
  if letter == guessed_letter:
    print("Right")
    guessed_word[index] = letter
  else:
    print("Wrong")

print(guessed_word)
