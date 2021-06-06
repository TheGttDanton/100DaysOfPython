import random
EASY_LIFE = 10
HARD_LIFE = 5

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")


def choose_number():
  return random.randint(1,100)

def set_difficulty():
  difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard'").lower()
  if difficulty_level == "easy":
    life = EASY_LIFE
  else:
    life = HARD_LIFE
  return life

def decrease_life():
  return life - 1

def check_guess(answer, number):
  if answer == number:
    print("Correct you guessed it right")
    return True
  elif answer > number:
    print("Too high")
    return False
  elif answer < number:
    print("Too low")
    return False


number = choose_number()
life = set_difficulty()
while life > 0:
  print(f"you have {life} attempts to guess")
  answer = int(input("guess the number"))
  if check_guess(answer, number):
    break
  else:
    print("guess again")
  life = decrease_life()
