MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

def report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(drink):
    flag = True
    for ingredient in MENU[drink]["ingredients"]:
        if not ingredient_check(drink, ingredient):
            flag = False
    return flag

def ingredient_check(drink, ingredient):
    check = MENU[drink]["ingredients"][ingredient] <= resources[ingredient]
    if not check:
        print(f"Sorry there is not enough {ingredient}.")
    return check

def coin_intake(cost):
    print("please insert coins.")
    total = int(input("How many quarters?: ")) *  0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - cost, 2)
        print(f"Here is ${change} dollars in change.”")
        return True

def make_drink(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

    print(f"Here is your {drink}. Enjoy!")


power = True
money = 0.00

while power:
    order = input("What you you like? (espresso, latte, cappuccino): ").lower()

    if order == "off":
        power = False
        break

    if order == "report":
        report(money)
        continue

    if order not in MENU:
        continue

    enough_resources = check_resources(order)

    #not enough resources
    if not enough_resources:
        if coin_intake(MENU[order]["cost"]):
            money += MENU[order]["cost"]
            make_drink(order)



