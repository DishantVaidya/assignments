# we can copy and paste content of one file to another like this

with open('file1.txt', 'r') as read_file:
    with open('file2.txt', 'w') as write_file:
        for line in read_file:
            write_file.write(line)


# This will copy the content of file1.txt to file2.txt  
# if you want to not overwrite the existing content of file2.txt, you can use 'a' mode instead of 'w' mode
'''          
with open('file1.txt', 'r') as read_file:
    with open('file2.txt', 'a') as write_file:
        for line in read_file:
            write_file.write(line)          

            '''