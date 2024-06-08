from domain import Latte, Espresso, Cappuccino
from services import receive_payment, deduct_resources, print_report_resources, verify_resources

def run():

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }

    print("----------------------------------------------------------------------")
    print("------------------ Welcome to the coffee machine! --------------------")
    print("----------------------------------------------------------------------")
    input_drink = input("What would you like? (1-Espresso/2-Latte/3-Cappuccino): ")
     
    if input_drink == "espresso":
        espresso = Espresso()
        deduct_resources(drink=espresso, resources=resources)
        if verify_resources(
            drink_method=espresso.make_drink, resources=resources, supply="water"
        ) == False:
            return
        money = receive_payment(drink_choice=espresso)
        
        if money[1]:
            espresso.make_drink()
    elif input_drink == "latte":
        latte = Latte()
        deduct_resources(drink=latte, resources=resources)
        money = receive_payment(drink_choice=latte)
        if money[1]:
            latte.make_drink()
    elif input_drink == "cappuccino":
        cappuccino = Cappuccino()
        deduct_resources(drink=cappuccino, resources=resources)
        money = receive_payment(drink_choice=cappuccino)
        if money[1]:
            cappuccino.make_drink()
    elif input_drink == "report":
        print(print_report_resources(resources))
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    run()

