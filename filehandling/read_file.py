handle_file = open("test.txt", "r")
"""Reads all the entire file module"""
data = handle_file.read()
"""Reads only the first line in the file module"""
#data = handle_file.readline()
"""Reads all lines in the file module"""
#data = handle_file.readlines()
print(data)
"""Closes our file module after reading"""
handle_file.close()