#program to print the number of prime numbers given by the user
try:
    n = int(input("How many prime numbers do you want:"))     #user input for the number of prime numbers to print

    if n <= 0:                                                #checks if the number is less than or equal to 0
        print("Please enter a number greater than 0.")
    else:                                                     #continue the loop if the number is greater than 0
        count = 0                                             
        num = 2          

        print("Prime numbers are:")                           #print the prime numbers
       
        while count < n:                                      # Loop to find and print the first n prime numbers

            
            prime = True                                      #assume the number is prime initially
            for i in range(2, num):                           # Loop to check if num is prime
                if num % i == 0:
                    prime = False

            if prime:                                         # If num is prime, it will be printed
                print(num)
                count += 1
            num += 1  

        print("Total prime numbers printed:", count)          #count of prime numbers printed

except ValueError:                                            #exception handling for invalid input
    print("Invalid input! Please enter a whole number like 5 or 10.")

#end of the program