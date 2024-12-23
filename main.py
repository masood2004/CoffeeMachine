import os
import sys
import animation as ani
from logo import logo
from resources import resources
from menu import MENU as menu


def coffee_machine():
    os.system("cls")
    print(logo)

    # Profit
    profit = 0

    # Resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    while True:  # Infinite loop to keep the machine running
        # Menu
        espresso = menu["espresso"]
        latte = menu["latte"]
        cappuccino = menu["cappuccino"]

        user_choice = input(
            "What would you like? [espresso(Rs. 400) / latte(Rs. 600) / cappuccino (Rs. 500)]: ").lower()

        if user_choice == "off":
            # Turn off the Machine.
            os.system("cls")
            print("Turning off the coffee machine. Goodbye!")
            sys.exit()

        elif user_choice == "report":
            # Give the report related to resources and profits.
            print(f"Water: {water}")
            print(f"Milk: {milk}")
            print(f"Coffee: {coffee}")
            print(f"Money: Rs.{profit}")

        elif user_choice == "fill":
            # Refill the resources
            water_to_add = int(
                input("How much water would you like to add (ml)?: "))
            milk_to_add = int(
                input("How much milk would you like to add (ml)?: "))
            coffee_to_add = int(
                input("How much coffee would you like to add (g)?: "))
            water += water_to_add
            milk += milk_to_add
            coffee += coffee_to_add
            print("Resources have been replenished!")

        else:
            ask_money = input(
                "Do you have coins or paper notes? (coins/paper/both): ").lower()

            def check_money():
                """This function checks the payment methods."""
                money_in_function = 0
                if ask_money == "coins":
                    coins = int(input("How many coins would you like?: "))
                    money_in_function += coins
                if ask_money == "paper":
                    papers = int(
                        input("How many paper money would you like?: "))
                    money_in_function += papers
                if ask_money == "both":
                    paper_first = int(input("Insert the paper money first: "))
                    money_in_function += paper_first
                    coins_first = int(input("Insert the coins now: "))
                    money_in_function += coins_first
                return money_in_function

            money = check_money()
            profit += money
            refund_money = 0

            # Latte as a User Choice
            if user_choice == "latte":
                if money >= latte["cost"]:
                    if water >= 200 and coffee >= 24 and milk >= 150:
                        print("Making Latte")
                        ani.bouncing_ball_animation(duration=3)
                        water -= 200
                        coffee -= 24
                        milk -= 150
                        print("Here is your latte. Enjoy!")
                        refund_money = money - latte["cost"]
                        if refund_money > 0:
                            print(f"Here is your change: Rs.{refund_money}")
                    else:
                        print("Sorry, there is not enough water, coffee, or milk.")
                        profit -= money
                else:
                    print("Sorry, there is not enough money to buy a Latte.")

            # Espresso as a User Choice
            elif user_choice == "espresso":
                if money >= espresso["cost"]:
                    if water >= 50 and coffee >= 18:
                        print("Making Espresso")
                        ani.bouncing_ball_animation(duration=3)
                        water -= 50
                        coffee -= 18
                        print("Here is your espresso. Enjoy!")
                        refund_money = money - espresso["cost"]
                        if refund_money > 0:
                            print(f"Here is your change: Rs.{refund_money}")
                    else:
                        print("Sorry, there is not enough water or coffee.")
                        profit -= money
                else:
                    print("Sorry, there is not enough money to buy an Espresso.")

            # Cappuccino as a User Choice
            elif user_choice == "cappuccino":
                if money >= cappuccino["cost"]:
                    if water >= 250 and coffee >= 24 and milk >= 100:
                        print("Making Cappuccino")
                        ani.bouncing_ball_animation(duration=3)
                        water -= 250
                        coffee -= 24
                        milk -= 100
                        print("Here is your cappuccino. Enjoy!")
                        refund_money = money - cappuccino["cost"]
                        if refund_money > 0:
                            print(f"Here is your change: Rs.{refund_money}")
                    else:
                        print("Sorry, there is not enough water, coffee, or milk.")
                        profit -= money
                else:
                    print("Sorry, there is not enough money to buy a Cappuccino.")

            else:
                print("Invalid choice. Please select a valid option.")

        # Add a break to give the user time before the next loop iteration
        input("\nThanks for coming ...")
        os.system("cls")
        print(logo)


coffee_machine()
