# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 00:05:27 2025

@author: suresh.burra
"""
from typing import List, Dict


class Equipment:
    def __init__(self, name: str, item_type: str, stats: Dict[str, int]):
        self.name = name
        self.item_type = item_type
        self.stats = stats


class Skill:
    def __init__(self, name: str, level: int, description: str):
        self.name = name
        self.level = level
        self.description = description


class GameCharacter:
    def __init__(self):
        self.name = None
        self.character_class = None
        self.race = None
        self.level = 1
        self.stats = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
        self.health = 100
        self.mana = 100
        self.equipment = {}
        self.inventory = []
        self.skills = []
        self.appearance = {}

    def __str__(self):
        return (f"Character: {self.name}\n"
                f"Class: {self.character_class}, Race: {self.race}, Level: {self.level}\n"
                f"Stats: {self.stats}\n"
                f"HP: {self.health}, Mana: {self.mana}\n"
                f"Skills: {[s.name for s in self.skills]}\n"
                f"Equipment: {list(self.equipment.keys())}")


class GameCharacterBuilder:
    def __init__(self, name: str):
        self.character = GameCharacter()
        self.character.name = name

    def set_class(self, character_class: str):
        self.character.character_class = character_class
        return self

    def set_race(self, race: str):
        self.character.race = race
        return self

    def set_level(self, level: int):
        self.character.level = level
        return self

    def set_stat(self, stat: str, value: int):
        if stat in self.character.stats:
            self.character.stats[stat] = value
        return self

    def set_stats(self, **stats):
        for stat, value in stats.items():
            if stat in self.character.stats:
                self.character.stats[stat] = value
        return self

    def set_health(self, health: int):
        self.character.health = health
        return self

    def set_mana(self, mana: int):
        self.character.mana = mana
        return self

    def equip_item(self, slot: str, equipment: Equipment):
        self.character.equipment[slot] = equipment
        return self

    def add_to_inventory(self, item: str):
        self.character.inventory.append(item)
        return self

    def add_skill(self, name: str, level: int, description: str):
        skill = Skill(name, level, description)
        self.character.skills.append(skill)
        return self

    def set_appearance(self, **appearance):
        self.character.appearance.update(appearance)
        return self

    def apply_class_template(self):
        """Apply class-specific defaults"""
        templates = {
            'warrior': {
                'stats': {'strength': 18, 'constitution': 16},
                'health': 150,
                'mana': 50
            },
            'mage': {
                'stats': {'intelligence': 18, 'wisdom': 16},
                'health': 80,
                'mana': 200
            },
            'rogue': {
                'stats': {'dexterity': 18, 'charisma': 14},
                'health': 100,
                'mana': 100
            }
        }

        template = templates.get(self.character.character_class.lower())
        if template:
            self.set_stats(**template['stats'])
            self.set_health(template['health'])
            self.set_mana(template['mana'])
        return self

    def build(self):
        if not self.character.name or not self.character.character_class:
            raise ValueError("Character must have a name and class defined.")
        return self.character

# Example Usage
weapon = Equipment("Excalibur", "sword", {"damage": 50, "strength": 5})
armor = Equipment("Dragon Armor", "chest", {"defense": 100, "constitution": 10})
character = (GameCharacterBuilder("Aragorn")
.set_class("Warrior")
.set_race("Human")
.set_level(20)
.apply_class_template()
.equip_item("weapon", weapon)
.equip_item("chest", armor)
.add_skill("Power Strike", 5, "Deals massive damage")
.add_skill("Shield Bash", 3, "Stuns enemy")
.set_appearance(hair="brown", eyes="blue", height="6'2")
.add_to_inventory("Health Potion")
.add_to_inventory("Mana Potion")
.build())
print(character)