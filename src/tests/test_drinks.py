from domain import Latte, Espresso, Cappuccino

def test_make_latte():
    
    expected = 200, 24, 150
    result = Latte().make_drink()

    assert result == expected

def test_make_espresso():
        
    expected = 50, 18, 0
    result = Espresso().make_drink()

    assert result == expected

def test_make_cappuccino():
    
    expected = 250, 24, 100
    result = Cappuccino().make_drink()

    assert result == expected