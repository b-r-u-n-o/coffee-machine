from domain import Latte, Espresso, Cappuccino
from services import verify_resources, deduct_resources, print_report_resources

latte = Latte()
espresso = Espresso()
cappuccino = Cappuccino()

def test_verify_resources_full_water():
    
    resources = {"water": 300}
    
    supply = "water"
    result = verify_resources(
        drink_method=latte.make_drink,
        resources=resources,
        supply=supply
    )
    
    excpected = True
    assert result == excpected

def test_verify_resources_low_water():
    
    resources = {"water": 10}
    
    supply = "water"
    result = verify_resources(
        drink_method=latte.make_drink,
        resources=resources,
        supply=supply
    )
    
    excpected = False
    assert result == excpected
    
def test_deduct_resources():
    
    resources = {"water": 300, "coffee": 100, "milk": 200}
    
    result = deduct_resources(
        drink=latte,
        resources=resources
    )
    
    excpected = {"water": 100, "coffee": 76, "milk": 50}
    assert result == excpected
    
def test_print_report_resources():
    
    resources = {"water": 300, "coffee": 100, "milk": 200}
    
    result = print_report_resources(resources)
    
    excpected = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
    )
    assert result == excpected