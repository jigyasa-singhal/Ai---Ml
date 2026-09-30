from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):   # include self
        pass

class Lion(Animal):         # inherit from Animal
    def make_sound(self):
        print("roar")

lion = Lion()
lion.make_sound()
