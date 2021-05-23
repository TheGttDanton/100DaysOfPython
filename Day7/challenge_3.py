import random

word_list = ["ardvark", "baboon", "camel"]

random_choice = random.choice(word_list)

guessed_word = ["_"] * len(random_choice)

print(f"the word chosen is {random_choice}")
print(*guessed_word)

lives = 3

while lives > 0 and '_' in guessed_word:
  guessed_letter = input("Guess a letter of the word \n").lower()

  is_guessed_correctly = False
  for (index, letter) in enumerate(random_choice):
    if letter == guessed_letter:
      print("Right")
      guessed_word[index] = letter
      is_guessed_correctly = True
    else:
      print("Wrong")
      
  if not is_guessed_correctly:
    lives -= 1
  print(*guessed_word)
  

if '_' in guessed_word:
  print("You loose")
else:
  print("You won")
