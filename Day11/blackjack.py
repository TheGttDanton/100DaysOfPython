import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def initiate_game():
  player_cards = random.choices(cards, k = 2)
  dealer_cards = random.choices(cards, k = 2)
  print(f"Your cards: {player_cards}")
  print(f"Dealer cards: {dealer_cards[0]} *")
  return player_cards, dealer_cards
  
def check_card_values(cards):
  values = 0
  for card in cards:
    if (values + card) > 21 and card == 11:
      values += 1
    else:
      values += card
  return values

def check_results(dealer_cards_value, player_cards_values):
  if dealer_cards_value > 21:
    print("you won")
  elif dealer_cards_value > player_cards_values:
    print("you lost")
  elif player_cards_values > dealer_cards_value:
    print("you won")
  else:
    print("draw")

def start_game():
  player_cards, dealer_cards = initiate_game()
  continue_picking = True
  while continue_picking:
    card_values = check_card_values(player_cards)
    if card_values > 21:
      print("You lost")
      return
    pick_card = input("Do you want to pick other card y - yes, n - no \n").lower()
    if pick_card == "n":
      continue_picking = False
    else:
      new_card = random.choice(cards)
      player_cards.append(new_card)
      print(f"your new cards: {player_cards}")
    player_cards_values = check_card_values(player_cards)
  print(f"dealer cards: {dealer_cards}")
  dealer_cards_value = check_card_values(dealer_cards)
  while dealer_cards_value < 17:
    print("Dealer picking new card")
    new_card = random.choice(cards)
    dealer_cards.append(new_card)
    print(f"dealer new cards: {dealer_cards}")
    dealer_cards_value = check_card_values(dealer_cards)
  check_results(dealer_cards_value, player_cards_values)
start_game()
