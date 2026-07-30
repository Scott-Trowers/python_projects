from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

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
        # 'report' and 'power_off' are secret options, not shown to the user
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
            print(f"One {selected_drink.name} is {money_processer.CURRENCY}{price:.2f}")
            has_paid = money_processer.make_payment(price)
        else:
            has_paid = False
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
