import data
import random

list = data.data
score = 0
should_countinue = True

# Get random user from list without repitition
def fetch_random_data():
  return random.choice(list)

# Create the question
def create_question(person):
  question = f"{person['name']}, {person['profession']}, from {person['country']}"
  return question

def format_question(person_a, person_b):
  question_a = "A." + create_question(person_a)
  question_b = "B." + create_question(person_b)
  print(question_a)
  print("OR")
  print(question_b)
  return input("Who is having more followers ? A or B").lower()

# decide answer
def decide_answer(person1, person2):
  if person1['followers'] > person2['followers']:
    return "a" , person_a
  else:
    return "b", person_b


person_a = fetch_random_data()
person_b = fetch_random_data()
while person_a == person_b:
  person_b = fetch_random_data()

while should_countinue:
  answer = format_question(person_a, person_b)
  correct_answer, person = decide_answer(person_a, person_b)
  if answer == correct_answer:
    score += 1
    person_a = person
    person_b = fetch_random_data()
    while person_a == person_b:
          person_b = fetch_random_data()
    print("correct")
  else:
    print("incorrect")
    should_countinue = False


print(f"Your final score is {score}")
