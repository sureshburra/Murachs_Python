class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        return None
    
pet = animal_factory("dog")
print(pet.speak())
pet = animal_factory("cat")
print(pet.speak())


