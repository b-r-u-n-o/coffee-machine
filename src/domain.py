# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

# interface
class MakeDrink(ABC):
    
    @abstractmethod
    def add_water(self):
        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def add_coffee(self):
        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def add_milk(self):
        raise NotImplementedError("This method is not implemented")
    
    @abstractmethod
    def add_money(self):
        raise NotImplementedError("This method is not implemented")

    @abstractmethod
    def make_drink(self):
        water = self.add_water()
        coffee = self.add_coffee()
        milk = self.add_milk()
        return water, coffee, milk

class Latte(MakeDrink):
    
    def add_water(self):
        return 200

    def add_coffee(self):
        
        return 24

    def add_milk(self):
        
        return 150
    
    def add_money(self):
        
        return 2.5
    
    def make_drink(self):
        water = self.add_water()
        coffee = self.add_coffee()
        milk = self.add_milk()
        money = self.add_money()
        
        return water, coffee, milk, money

class Cappuccino(MakeDrink):
    
    def add_water(self):
        return 250

    def add_coffee(self):
        
        return 24

    def add_milk(self):
        
        return 100
    
    def add_money(self):
        
        return 2.75
    
    def make_drink(self):
        water = self.add_water()
        coffee = self.add_coffee()
        milk = self.add_milk()
        money = self.add_money()
        
        return water, coffee, milk, money

class Espresso(MakeDrink):
    
    def add_water(self):
        return 50

    def add_coffee(self):        
        return 18

    def add_milk(self):
        
        return 0
    
    def add_money(self):
        
        return 1.5
    
    def make_drink(self):
        water = self.add_water()
        coffee = self.add_coffee()
        milk = self.add_milk()
        money = self.add_money()
        
        return water, coffee, milk, money

# class Supplies:

#     def __init__(self):
#         self._water = 300
#         self._coffee = 100
#         self._milk = 200

#     @property
#     def get_water(self):
#         return self._water
    
#     @get_water.setter
#     def set_water(self, value):
#         self._water = value
    
#     def coffee(self):
#         return 100

#     def milk(self):
#         return 200

class Coins:
    
    @property
    def penny(self):
        return 0.01
    
    @property
    def nickel(self):
        return 0.05
    
    @property
    def dime(self):
        return 0.10
    
    @property
    def quarter(self):
        return 0.25