class programmer:
    company = "Google"

    def __init__(self,name,age):
        self.name = name
        self.age = age

A = programmer("Dishant", 18)
print(A.name, A.age, A.company)

B = programmer("Harry", 19)
print(B.name, B.age, B.company)
