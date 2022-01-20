# Ruben Sanduleac
# Description: This is a secret auction program

from ui import logo
from clear_function import clear

# print the logo for the program
print(logo)

# auction dictionary
auction = {}
while True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    auction[name] = bid
    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    clear()
    if again == "no":
        break
winner = "0"
winner_name = ''
for amount in auction:
    if auction[amount] > winner:
        winner = auction[amount]
        winner_name = amount

print(f"The winner is {winner_name} with a bid of ${winner}")
