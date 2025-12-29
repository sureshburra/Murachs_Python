# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 16:13:07 2025

@author: suresh.burra
"""

from typing import List

class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.cheese = None
        self.toppings: List[str] = []
        self.sauce = None
        self.extra_cheese = False
        
    def __str__(self):
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return (f"{self.size} Pizza with {self.crust} crust, {self.sauce} sauce, "
                f"{self.cheese} cheese, toppings: {toppings_str},"
                f"Extra cheese: {self.extra_cheese}"
                )
    
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
        
    def set_size(self, size):
        valid_sizes = ['small', 'medium', 'large', 'extra-large']
        if size.lower() not in valid_sizes:
            raise ValueError(f"Size must be one of {valid_sizes}")
        self.pizza.size = size
        return self
    
    def set_crust(self, crust):
        self.pizza.crust = crust
        return self
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    
    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def add_toppings(self, *toppings):
        self.pizza.toppings.extend(toppings)
        return self
    
    def add_extra_cheese(self):
        self.pizza.extra_cheese = True
        return self
    
    def build(self):
        if not self.pizza.size:
            raise ValueError("Pizza size must be set")
        if not self.pizza.crust:
            self.pizza.crust = "regular"
        if not self.pizza.sauce:
            self.pizza.sauce = "tomato"
        if not self.pizza.cheese:
            self.pizza.cheese = "mozzarella"
        return self.pizza
    
    
# Usage
pizza = (PizzaBuilder().set_size("large")
         .set_crust("thin").set_sauce("tomato")
         .set_cheese("mozzarella")
         .add_toppings("pepperoni", "mushrooms", "olives")
         .add_extra_cheese()
         .build()
    )

print(pizza)