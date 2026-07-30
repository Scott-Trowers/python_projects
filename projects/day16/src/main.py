from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

'''
1) prompt user
2) options:
    a) 'off' -> end execution
    b) 'report' -> show current resources
    c) 'espresso/latte/cappuccino' -> begin making drink
3) begin making drink:
    a) check enough resources to make selected drink
        i) if not, show an error message
    b) take payment:
        i) prompt payment (as input) until cost is covered
        ii) if too much given, return change
        iii) record to resources
    c) make the drink:
        i) deduct resources
        ii) output drink
4) reset for next customer    
'''
menu = Menu()
coffee_maker = CoffeeMaker()
money_processer = MoneyMachine()

is_on = True
while is_on:

    # prompt user
    drink_options = menu.get_items().split('/')
    all_options = ['off', 'report'] + drink_options
    selected_option = ''
    while selected_option not in all_options:
        selected_option = str(input(f"What would you like?\n{' '.join(drink_options)}\n")).lower()

    print('-----------------')

    if selected_option == 'off':
        is_on = False
    elif selected_option == 'report':
        coffee_maker.report()
        money_processer.report()
    else:
        selected_drink = menu.find_drink(selected_option)
        has_resources = coffee_maker.is_resource_sufficient(selected_drink)

        if has_resources:
            price = selected_drink.cost
            print(f"One {selected_drink.name} is ${price:.2f}")
            has_paid = money_processer.make_payment(price)
        else:
            print(f"Sorry, {selected_drink} is currently unavailable.")

        print('-----------------')

        if has_resources and has_paid:
            print(f"One {selected_drink.name} coming right up!")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            coffee_maker.make_coffee(selected_drink)

    print('-----------------')
