from abc import ABC,abstractmethod

class Animal:
    
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    
    def speak(self):
        return 'Woof!'
    
class Cat(Animal):
    
    def speak(self):
        return 'Meow'
    
dog = Dog()

print(dog.speak())

cat = Cat()

print(cat.speak())