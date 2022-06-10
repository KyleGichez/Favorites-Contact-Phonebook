#File handling in python
handle_file = open("test.txt", "r")
"""Reads all the entire file module"""
data = handle_file.read()
"""Reads only the first line in the file module"""
data = handle_file.readline()
"""Reads all lines in the file module"""
data = handle_file.readlines()

"""Looping through a file and checking how many times the python keyword is present"""
counter = 0
for word in data.split():
    if word == "python":
        counter += 1
    print(counter)
    
print(data)
"""Closes our file module after reading"""
handle_file.close()

#Using with operator to read a file
with open("test.txt", "r") as handle:
    data = handle.read()
"""Loop through our lorem.txt file and check instances of the word lorem"""
counter = 0 
for word in data.split():
    if word == "python":
        counter += 1
        print(counter)
print(data)
print(len(data))

#Writing a new text file 
handle_file = open("testfile.txt", "w")
"""Creates a new file with the name testfile.txt in our working folder"""
data = handle_file.write("Sexy Ms Dollar Baby you are making bold moves everyday.")
handle_file.close()