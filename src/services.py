from domain import Coins

def verify_resources(drink_method: str, resources: dict, supply: str) -> bool:

    # TODO: Refactor this function to be more generic
    for i in range(1, len(drink_method())):
        sup = resources[supply] - drink_method()[i]

        if sup < 0:
            print(f"Sorry there is not enough {supply}.")
            return False
        return True

def deduct_resources(drink:object, resources: dict):

    drink = drink
    resources["water"] -= drink.add_water()
    resources["coffee"] -= drink.add_coffee()
    resources["milk"] -= drink.add_milk()
    # resources["money"] += drink.cost

    return resources

def print_report_resources(resources: dict):

    return (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
    )
    # print(f"Money: ${resources['money']}")
    
def receive_payment(drink_choice: object) -> float:
    
    c = Coins()
    drink_price = drink_choice.make_drink()[3]
    
    penny_input = int(input("How many pennies?: "))   
    nickel_input = int(input("How many nickels?: "))
    dime_input = int(input("How many dimes?: "))
    quarter_input = int(input("How many quarters?: "))
         
    calculate = (
        (penny_input * c.penny) 
        + (nickel_input * c.nickel) 
        + (dime_input * c.dime) 
        + (quarter_input * c.quarter)
    )
    
    if calculate < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return calculate, False
    elif calculate > drink_price:
        print(f"Here is ${calculate - drink_price} in change.")
        return calculate, True    
    else:
        print(f"Here is your drink ☕ enjoy!")
        return calculate, True
    
        
            
    
