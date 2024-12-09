import sys
from resources import resources
from menu import MENU as menu

# Profit
money = 0

# Resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

# Menu
espresso = menu["espresso"]
latte = menu["latte"]
cappuccino = menu["cappuccino"]


user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

ask_money = input("Do you have coins or paper notes? (coins/paper/both): )").lower()

def check_money():
    money_in_function = 0
    if ask_money == "coins":
        coins = int(input("How many coins would you like?: "))
        money_in_function += coins
    if ask_money == "paper":
        papers = int(input("How many paper money would you like?: "))
        money_in_function += papers
    if ask_money == "both":
        paper_first = int(input("Insert the paper money first: "))
        money_in_function += paper_first
        coins_first = int(input("Insert the coins now: "))
        money_in_function += coins_first
    return money_in_function

money += check_money()

if user_choice == "off":
    sys.exit()
if user_choice == "report":
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")
if user_choice == "latte":
    if  water >= 200 and coffee >= 24 and milk >= 150:
        print("Making Latte")
        water -= 200
        coffee -= 24
        milk -= 150
        money += latte["cost"]
    elif water < 200 or coffee < 24 or milk < 150:
        print("Sorry, there is not enough water or coffee or milk.")
if user_choice == "espresso":
    if water >= 50 and coffee >= 18:
        print("Making Espresso")
        water -= 50
        coffee -= 18
        money += espresso["cost"]
    elif water < 50 or coffee < 18:
        print("Sorry, there is not enough water or coffee.")
if user_choice == "cappuccino":
    if water >= 250 and coffee >= 24 and milk >= 100:
        print("Making Cappuccino")
        water -= 250
        coffee -= 24
        milk -= 100
        money += cappuccino["cost"]
    elif water < 250 or coffee < 24 or milk < 100:
        print("Sorry, there is not enough water or coffee or milk.")
# while True:
#     user_choice = input("What would you like? (espresso/latte/cappuccino): ")
