#Assignment:
#Create a class Dog with instance variables name and breed. Add an instance method bark() 
#that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Example usage:
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()