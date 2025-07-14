class college:
    name= "DG Ruparel College"

    def display(self):
        print("College Name:", self.name)

class student(college): #single inheritance
    def info(self):
        print("Student Name: Dishant")
        print("Student Age: 18")
        print("Student Division: A")

A = student() #no need to make object of college class as student is inheriting from college
A.display() 
A.info()    
