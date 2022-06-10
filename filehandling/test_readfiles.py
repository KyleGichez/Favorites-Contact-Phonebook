import unittest 
import readfiles

class TestReadFiles(unittest.TestCase):
    """
    Test the functions on the readfile module
    The unittest.TestCase arguement represents a class from the unittest module to create unittests.
    """

    def test_get_data(self):
        """Test get data from our readfiles module"""
        with open("lorem.txt", "r") as handle:
            data = handle.read()
            self.assertEqual(data, readfiles.read_file("lorem.txt"))

    def test_none_file(self):
        """Test check if we entered a wrong file path: Here we check if an assertion is raised when a wrong file is inputted."""
        self.assertEqual(None, readfiles.read_file(""))

    def test_longest_word(self):
        """Test check for the longest word"""
        txt_file = "lorem.txt"
        with open(txt_file, "r") as handle:
            data = handle.readlines()
            for word in data:
                return len(word)
        self.assertEqual(data, readfiles.read_file("lorem.txt"))

if __name__ == '__main__':
    unittest.main()