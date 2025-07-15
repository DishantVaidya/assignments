class employee:
    count = 10
    @classmethod # <--- This is a class method, it is used to access class variables
    def show(cls):
        print(f"Employees number : {cls.count}")

    @property # <--- This is a property, it allows you to access the method like an attribute
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter # <--- This is a setter for the property, it allows you to set the value
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]

a = employee()
a.count = 100
a.name = "John Doe"
a.show()
print(f"First Name: {a.fname}, Last Name: {a.lname}")