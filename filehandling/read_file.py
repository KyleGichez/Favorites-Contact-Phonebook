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