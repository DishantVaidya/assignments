#opening and writing to a file

with open('file1.txt', 'w') as file:
    file.write("Hello World!\n") # Writing a string to the file and it will overwrite the existing content
    file.write("This is File 1.\n") 

#creating a list and writing it to the file
lines=["hello this is line 1 \n","Hello this is line 2 \n","Hello this is line 3 \n"] #list of strings

#for single line we can use this
with open('file1.txt', 'w') as file:
    file.write(lines[1])  # Writing the second line from the list to the file by indexing

#or By looping through the list, we can write each line to the file
with open('file1.txt', 'w') as file:
    for line in lines:
        file.write(line)

#for not overwriting the existing content, but adding new line we can use 'a' mode which stands for append

with open('file1.txt', 'a') as file:
    file.write("This is an appended line.\n")  # Appending a new line to the file and will not overwrite the existing content

