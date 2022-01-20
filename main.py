# Ruben Sanduleac
# Description: This is a secret auction program

from ui import logo

# print the logo for the program
print(logo)

# auction dictionary
auction = {}
while True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    auction[name] = bid
    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if again == "no":
        break
