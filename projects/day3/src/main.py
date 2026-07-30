from menu_and_resources import MENU, resources
import sys
import time

def option_menu():
    options = {
        1: 'espresso',
        2: 'latte',
        3: 'cappuccino',
        4: 'report',
        5: 'power_off',
    }

    # 'report' and 'power_off' are secret options, not shown to the user
    option_selected = 0
    print("Options:")
    print("    1 - espresso\n    2 - latte\n    3 - cappuccino")
    while not (1 <= option_selected <= 5):
        try:
            option_selected = int(input("Select Option: "))
        except ValueError:
            print("Please enter an valid (integer) option.")

    option_item = options[option_selected]

    return option_item


def power_off():
    print("Shutting down ...")
    sys.exit()


def report(resources):
    print("Resources:")
    print(f"   Water: {resources['water']}ml")
    print(f"   Milk: {resources['milk']}ml")
    print(f"   Coffee: {resources['coffee']}g")
    print(f"   Money: £{resources['money']:.2f}")
    print("------------")


def check_resources(item, resources):
    reqs = MENU[item]["ingredients"]
    enough_resources = True

    for resource, amount in reqs.items():
        if amount > resources[resource]:
            print(f"Sorry, not enough {resource}!")
            enough_resources = False

    return enough_resources


def charge_customer(item, resources):
    price = MENU[item]['cost']

    print(f"Item: {item}\nPrice: £{price:.2f}")

    payment = 0
    remaining_price = price - payment
    while remaining_price > 0:
        try:
            payment += float(input(f"Please insert £{remaining_price:.2f}: "))
        except ValueError:
            print("Please enter a numeric value.")
        remaining_price = price - payment

    print("Payment Successful!")
    time.sleep(0.75)

    # return payment when remaining_price is exceeded, by 'adding' the negative back to payment
    if remaining_price < 0:
        print(f"Returning Change: £{-1 * remaining_price:.2f}")
        payment += remaining_price

    resources["money"] += payment

    return resources


def make_drink(item, resources):
    recipe = MENU[item]["ingredients"]

    for resource, amount in recipe.items():
        resources[resource] -= amount

    print(f"One {item} coming right up! Please wait...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print(f"Please find your {item} below! Enjoy!")
    print("------------")

    return resources

def coffee_machine(resources):

    while True:
        print("Welcome!")
        time.sleep(1)

        option_selected = option_menu()

        print("------------")

        if option_selected in ['espresso', 'latte', 'cappuccino']:
            enough_resources = check_resources(option_selected, resources)
            if enough_resources:
                resources = charge_customer(option_selected, resources)
                resources = make_drink(option_selected, resources)
        elif option_selected == 'report':
            report(resources)
        elif option_selected == 'power_off':
            power_off()

        time.sleep(3)
        print(20 * '\n')
        print("------------")


coffee_machine(resources)
