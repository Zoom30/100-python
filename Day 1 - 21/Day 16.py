from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# my_screen.screensize(600, 600, 'green')
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.rt(90)
# timmy.forward(200)
# print(timmy.position())
# my_screen.exitonclick()

# =================================================================================

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align["Pokemon Name"] = "l"
# print(table)
# print(table)

# =====================================================================================
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
# is_on = True
# coffee_maker.report()
# money_machine.report()
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
