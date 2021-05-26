print("Welcome to the secret bidding")

add_new_bidder = True
bidding = []

while add_new_bidder:
  name = input("What is you name ? \n")
  amount = int(input("Enter your bid in $ \n"))
  bid = {
    "name": name,
    "amount": amount
  }
  bidding.append(bid)
  
  show_add_new = input("Any other bidder ? y or n").lower()
  
  if show_add_new != "y":
    add_new_bidder = False

highest_bidder_name = ""
highest_bidder_amount = 0

for bid in bidding:
  name = bid["name"]
  amount = bid["amount"]
  
  if amount > highest_bidder_amount:
    highest_bidder_amount = amount
    highest_bidder_name = name


print(f"The highest bidder is {highest_bidder_name} with amount {highest_bidder_amount}")
