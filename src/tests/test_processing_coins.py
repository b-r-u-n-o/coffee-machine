from domain import Latte, Cappuccino, Espresso
from domain import Coins
from services import receive_payment

# coins
c = Coins()

latte = Latte()
cappuccino = Cappuccino()
espresso = Espresso()

def test_processing_received_coins_for_latte():
    
    price = latte.make_drink()[3]    
    received = (10 * c.penny) + (8 * c.nickel) + (10 * c.dime) + (4 * c.quarter)
    
    assert price == received
    
    
def test_processing_received_less_coins_for_latte():
    
    price = latte.make_drink()[3]   
    received = (2 * c.penny) + (8 * c.nickel) + (10 * c.dime) + (2 * c.quarter)
    
    assert price > received
    
def test_processing_received_more_coins_for_latte():
    
    price = latte.make_drink()[3]    
    received = (10 * c.penny) + (8 * c.nickel) + (11 * c.dime) + (5 * c.quarter)
    
    assert price < received

def test_analysing_received_more_coins_for_latte():
    
    qt_penny = 10
    qt_nickel = 8
    qt_dime = 11
    qt_quarter = 5 
    
    expected = (10 * c.penny) + (8 * c.nickel) + (11 * c.dime) + (5 * c.quarter)
    received = receive_payment(
        qt_penny, 
        qt_nickel, 
        qt_dime, 
        qt_quarter, 
        latte
    )
    
    assert expected == received

def test_analysing_received_less_coins_for_latte():
    
    qt_penny = 2
    qt_nickel = 8
    qt_dime = 10
    qt_quarter = 2
    
    expected = (2 * c.penny) + (8 * c.nickel) + (10 * c.dime) + (2 * c.quarter)
    received = receive_payment(
        qt_penny, 
        qt_nickel, 
        qt_dime, 
        qt_quarter, 
        latte
    )
    
    assert expected == received