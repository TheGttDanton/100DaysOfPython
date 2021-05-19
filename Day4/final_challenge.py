import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

map = [rock, paper, scissors]
choice = int(input("Enter your choice. 0 - Rock  1 - paper 2 - scissors"))

your_choice = map[choice]
  
print(f"you choose \n {your_choice}")

computer_choice = random.choice(map)

print(f"computer choose \n {computer_choice}")


if your_choice == computer_choice:
  print("Draw")
elif your_choice == rock:
  if computer_choice == scissors:
    print("you win")
  else:
    print("you loose")
elif your_choice == paper:
  if computer_choice == rock:
    print("you win")
  else:
    print("you loose")
else:
  if computer_choice == paper:
    print("you win")
  else:
    print("you loose")
