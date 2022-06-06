# Favorites Contact Phonebook
This is a software program for managing your favorite contacts in your phonebook that I coded to enhance my python coding skills through implementing the use of  classes, Behaviour Driven Development and test_cases for Test Driven Development to build this software program.
I have coded this Favorites Contact Phonebook project in python3. Let's have a look at my work! :wave:

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
- [Author](#author)

## Overview
To install this project in your local repository / working environment, you need to clone this repository using git clone commandline:
````Using git clone
git clone https://github.com/KyleGichez/Favorites-Contact-Phonebook
````
After cloning this project repository into your local machine, extract the files in the folder to access the code.
Yes! You did that? Let's get started: 🚶‍♂️ 

### The challenge

You should be able to build a Favorites Contact Phonebook with the following features:

- Creates a contact.
- Saves a contact.
- Saves multiple contacts.
- Displays all contacts.
- Deletes a contact.
- Finds a contact by number.
- Exits the contact phonebook.


### Links

- Solution URL: [GitHub](https://github.com/KyleGichez/Favorites-Contact-Phonebook)

## My process

### Built with

- Python3

### What I learned

I have learned how to write test cases for Test Driven Development for my software program
```Python3
import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    def setUp(self):
        """test create new contact instance"""
        self.new_contact = Contact("James", "Muriuki", "07122329112", "james@msn.com")

    def test_init(self):
        """test init contact"""
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "07122329112")
        self.assertEqual(self.new_contact.email, "james@msn.com")
```
First we import unittest from python
Then we import the Contact class from the contact module where our code is written
After importing our module dependencies, now we start writing test cases for our program.
```Python3
class TestContact(unittest.TestCase):
```
First, we write test cases for our Contact class as seen in the code above
```Python3
 def setUp(self):
        """test create new contact instance"""
        self.new_contact = Contact("James", "Muriuki", "07122329112", "james@msn.com")
```
Then we write a setUp() function and pass in self as our arguement.It represents our contact class from which we create new instances for our class object.
Next, we create a new contact object with first name, last name, phone number and email properties. We create these contexts using self with the (.)dot notation as seen in the code above.
```Python3
def test_init(self):
```
We then write test cases for our object initialization and pass in self as our arguement as seen above.
```Python3
self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "07122329112")
        self.assertEqual(self.new_contact.email, "james@msn.com")
```
Next, we use the self.assertEqual() method to check if the arguements in our object initialization are equal to the arguements passed in when creating a new contact object.
```Python3
 def tearDown(self):
        Contact.contact_list = []
```
I have also learned how to use the tearDown() method to check if all test cases for the saved phone number instances are equal when saving new contacts.
The tearDown() method initializes the contact list to an empty list after saving a contact and checks if it has already been saved.
......more test cases follow here..... You can see them in the phonebook_test.py module......
## Author

- Website - [Gichure Maina](https://www.linkedin.com/in/gichure-maina-a45aab202/)
- Frontend Mentor - [@KyleGichez](https://www.frontendmentor.io/profile/KyleGichez)
- Twitter - [@KyleGichez](https://www.twitter.com/KyleGichez)

