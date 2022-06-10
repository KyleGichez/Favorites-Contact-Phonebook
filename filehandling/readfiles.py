#We would like to read the file
#We would like to see how many times a single word is being used.
#We would like to see how many lines we have in our text files
#We would like to see the longest word in the text file.
#Write test cases for your file handling

"""Create a new variable to store the file that we need to open and read"""
text_file = "lorem.txt"

"""Function to read the file and return the data: This function creates a pass test_case for test_get_data() function."""
def read_file(text_file):
    with open(text_file, "r") as handle:
        data = handle.read()
        return data

def read_file(text_file):
    try:
        with open(text_file, "r") as handle:
            data = handle.read()
            return data
    except FileNotFoundError:
        return None

def longest_word(text_file):
    with open(text_file, "r") as handle:
        data = handle.readlines()
    for word in data:
        return len(word)

