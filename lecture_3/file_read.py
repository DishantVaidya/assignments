#opening file in read mode

file=open('file1.txt', 'r')
file.close()  # Don't forget to close the file after you're done

#or you can use the 'with' statement which automatically closes the file after the block is executed
with open('file1.txt', 'r') as file:
    print(file.read())

#this will close the file automatically after the block is executed

#readline mehthod

with open('file1.txt', 'r') as file:
    print(file.readline())  # Reads the first line
    print(file.readline())  # Reads the second line

#or you can use a loop to read all lines one by one
with open('file1.txt', 'r') as file:    
    for line in file:
        print(line.strip())  # .strip() removes the newline character at the end of each line

#readlines method

with open('file1.txt', 'r') as file:
    file_stuff=file.readlines() 
    print(file_stuff)  # Reads all lines into a list

    
