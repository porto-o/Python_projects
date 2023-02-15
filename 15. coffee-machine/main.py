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
    "Money": 0
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}


def main():
    # TODO
    # Prompt user for order
    order = input("What would you like? ")
    # First case: 'off'
    if order == 'off':
        shut_down()
    # Second case: 'report'
    elif order == 'report':
        print_report()
    # Otherwise
    else:
        # TODO
        # Check resources for the drink
        if check_resources(order):
            # Prompt to insert coins
            get_coins(order)
            resources_deduction(order)
            give_order(order)
        else:
            main()


def shut_down():
    print("Turning off the machine...")


def print_report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    main()


def check_resources(order):
    order_ingredients = {
        "water": MENU[order]["ingredients"]["water"],
        "milk": MENU[order]["ingredients"]["milk"],
        "coffee": MENU[order]["ingredients"]["coffee"]
    }

    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}")
            return False

    return True


def get_coins(order):
    total = 0
    price_order = MENU[order]["cost"]

    for item in coins:
        quantity = float(input(f"How many {item}? "))
        total += coins[item] * quantity

    if total < price_order:
        print("Sorry, that's not enough money. Money refunded.")
        main()

    print(f"Your change is {round(total - price_order, 2)}")
    resources["Money"] += float(MENU[order]["cost"])
    return True


def resources_deduction(order):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]


def give_order(order):
    print(f"Here is your {order}. Enjoy! ☕")
    main()


if __name__ == '__main__':
    main()
