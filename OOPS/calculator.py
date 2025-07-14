import math

class calculator:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(f"The sum of {self.num1} and {self.num2} is : {self.num1 + self.num2}")

    def square(self):
        print(f"The square of {self.num1} is : {self.num1 ** 2}")
        print(f"The square of {self.num2} is : {self.num2 ** 2}")   

    def squareroot(self):
        print(f"The square root of {self.num1} is : {math.sqrt(self.num1)}")
        print(f"The square root of {self.num2} is : {math.sqrt(self.num2)}")

A = calculator(3, 20)
A.add()
A.square()
A.squareroot()