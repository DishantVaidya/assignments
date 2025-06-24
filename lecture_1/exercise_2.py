
# Check if the number is prime or composite

n = int(input("Enter a number:")) #user input for the number

if n <= 1: #checks if the number is less than or equal to 1
    print("The number should be greater than 1.") 

else: 
    c = False #continue the loop if the number is greater than 1

    for i in range(2,n): #loop through numbers from 2 to n
        if n%i == 0:
            c = True    #continue the loop if n is divisible by i

if c:
    print("The given number is a composite number.")

else:
    print("The given number is a prime number.")                
#end of the program