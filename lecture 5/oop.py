# Define a class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object
my_dog = Dog(input("Enter the dog's name: "))

# Call the method
my_dog.bark()
