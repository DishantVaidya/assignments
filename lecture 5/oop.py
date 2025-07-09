# Create a class first
class student:
    division= "A"
    adress = "Mumbhai, India."

#creating an object 1 i.e. a student    
dishant = student()
dishant.name = "Dishant"

#creating an object 2 i.e. another student
gandharva = student()
gandharva.name = "Gandharva"

#printing student details
print("Name of the student :",dishant.name,"\n ","class :", dishant.division,", Region :", dishant.adress)
print("Name of the student :",gandharva.name,"\n ","class :", gandharva.division,", Region :", gandharva.adress)

#end of code
