# Swap two numbers using XOR
a = int(input("Enter the first number: "))        #user input for first number
b = int(input("Enter the second number: "))       #user input for second number

print("Original numbers are : a:", a, ", b:", b)  #printing original numbers

#logic to swap numbers using XOR
a = a ^ b                                         #a will xor b
b = a ^ b                                         #now b will be original a
a = a ^ b                                         #now a will be original b

print("After swapping: a:", a, ", b:", b)         #printing swapped numbers

#end of the program