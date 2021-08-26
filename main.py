MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffeeMachine_is_working = True
is_continue = True
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def check_sufficient(item):
    # def check_sufficient(water1, milk1, coffee1):

    global water, milk, coffee, is_continue
    # if water1 <= water:
    #     water = left_water
    # else:
    #     print("Sorry there is not enough water.")
    #     is_continue =  False
    # if milk1 <= milk:
    #     milk = left_milk
    # else:
    #     print("Sorry there is not enough milk.")
    #     is_continue =  False
    # if coffee1 <= coffee:
    #     coffee = left_coffee
    # else:
    #     print("Sorry there is not enough coffee.")
    #     is_continue =  False
    for item in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_continue =  False



def check_transaction(cost):
    global money

    required_cost = MENU[user_choice]["cost"]
    if cost >= required_cost:
        money += cost
        changes = round(cost - required_cost, 2)
        print(f"Here is ${changes} in change.")
        print(f"Here is your {user_choice} Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


while coffeeMachine_is_working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        coffeeMachine_is_working = False
    elif user_choice == "report":
        print(f'Water: {water}')
        print(f'Milk: {milk}')
        print(f'Coffee: {coffee}')
        print(f'Money: {money}')
    else:
        user_water = MENU[user_choice]["ingredients"]["water"]
        user_coffee = MENU[user_choice]["ingredients"]["coffee"]
        user_milk = MENU[user_choice]["ingredients"]["milk"]
        left_water = water - user_water
        left_coffee = coffee - user_coffee
        left_milk = milk - user_milk
        check_sufficient(MENU[user_choice]["ingredients"])
        if is_continue:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            check_transaction(total)







