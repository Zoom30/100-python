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
is_working = True
money = 0
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def calculate_amount(no_qs, no_ds, no_ns, no_ps):
    total_qs = no_qs * quarters
    total_ds = no_ds * dimes
    total_ns = no_ns * nickles
    total_ps = no_ps * pennies
    total = sum([total_qs, total_ds, total_ns, total_ps])
    return total


def process_request(drink_request):
    drink_water_amount = MENU[drink_request]["ingredients"]["water"]
    if drink_request == "espresso":
        drink_milk_amount = 0
    else:
        drink_milk_amount = MENU[drink_request]["ingredients"]["milk"]
    drink_coffee_amount = MENU[drink_request]["ingredients"]["coffee"]
    drink_price = float(MENU[drink_request]["cost"])

    if resources["water"] >= drink_water_amount and resources["milk"] >= drink_milk_amount and resources[
        "coffee"] >= drink_coffee_amount:
        print(f"It will be ${drink_price}")
        qrs = int(input("How many quarters: "))
        dms = int(input("How many dimes: "))
        nks = int(input("How many nickles: "))
        pns = int(input("How many pennies: "))

        payment = calculate_amount(no_qs=qrs, no_ds=dms, no_ns=nks, no_ps=pns)
        if payment >= drink_price:
            resources["water"] -= drink_water_amount
            resources["milk"] -= drink_milk_amount
            resources["coffee"] -= drink_coffee_amount
            change = payment - drink_price
            global money
            money += drink_price
            if change > 0:
                print(f"Here is your {drink_request}, change of ${round(change, 2)}")
            else:
                print(f"Here is your {drink_request}")
        else:
            print("Sorry, not enough money. Money refunded.")
    else:
        if resources["water"] < drink_water_amount:
            print("Sorry, not enough water")
        elif resources["milk"] < drink_milk_amount:
            print("Sorry, not enough milk")
        elif resources["coffee"] < drink_coffee_amount:
            print("Sorry, not enough coffee")


while is_working:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == "off":
        is_working = False
    elif request == "report":
        water_amount = resources["water"]
        milk_amount = resources["milk"]
        coffee_amount = resources["coffee"]
        print(f"Water: {water_amount}\nMilk: {milk_amount}\nCoffee: {coffee_amount}")
    else:
        process_request(request)
