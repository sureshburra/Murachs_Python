# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:48:08 2025

@author: suresh.burra
"""

from abc import ABC, abstractmethod

class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None
        self.interior = None
        self.rooms = 0
        
    def __str__(self):
        return (f"House: Foundation={self.foundation}, Structure={self.structure}, "
                f"Roof={self.roof}, Interior={self.interior}, Rooms={self.rooms}")
    

class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()
        
    @abstractmethod
    def build_foundation(self):
        pass
    
    @abstractmethod
    def build_structure(self):
        pass
    
    @abstractmethod
    def build_roof(self):
        pass
    
    @abstractmethod
    def build_interior(self):
        pass
    
    def get_house(self):
        return self.house
    
    
class ModernHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Concrete and Steel"
        return self
    
    def build_structure(self):
        self.house.structure = "Steel frame"
        self.house.rooms = 4
        return self
    
    def build_roof(self):
        self.house.roof = "Flat roof with solar panels"
        return self
    
    def build_interior(self):
        self.house.interior = "Modern minimalist"
        return self
    
    
class VictorianHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "Brick and mortar"
        return self
    
    def build_structure(self):
        self.house.structure = "Wooden frame"
        self.house.rooms = 6
        return self
    
    def build_roof(self):
        self.house.roof = "Pitched roof with tiles"
        return self
    
    def build_interior(self):
        self.house.interior = "Victorian ornate"
        return self
    
class ConstructionDirector:
    def __init__(self, builder):
        self.builder = builder
        
    def construct_house(self):
        return (self.builder
                .build_foundation()
                .build_structure()
                .build_roof()
                .build_interior()
                .get_house()
                )
    
# Usage
modern_builder = ModernHouseBuilder()
director = ConstructionDirector(modern_builder)
modern_house = director.construct_house()
print(modern_house)

victorian_builder = VictorianHouseBuilder()
director = ConstructionDirector(victorian_builder)
victorian_house = director.construct_house()
print(victorian_house)