#Create a phone book address with the following features.
#Adds a new contact
#saves a new contact
#saves multiple conntacts
#deletes a contact
#finds contact by number
#checks if number exits
#displays all contacts
#Exits the phonebook

import pyperclip
class Favorites:
    """ Empty contact list """
    favorites_list = []
    def __init__ (self, first_name, last_name, phone_number, email):
        """Initialize all the instances of the Favorites class"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        """Save a contact"""
        self.favorites_list.append(self)

    def delete_contact(self):
        """Delete a contact"""
        self.favorites_list.remove(self)

    @classmethod
    def find_contact_by_number(cls, number):
        """Find a contact by searching the phone number"""
        for contact in cls.favorites_list:
            if contact.phone_number == number:
                return contact
        return None

    @classmethod
    def contact_exists(cls, number):
        """Check if a contact exists"""
        for contact in cls.favorites_list:
            if contact.phone_number == number:
                return True
        return None

    @classmethod
    def display_contacts(cls):
        """Display all contacts"""
        print(cls.favorites_list)
        return cls.favorites_list

    @classmethod
    def copy_email(cls, number):
        """Copy and paste email adress"""
        found_contact = Favorites.find_contact_by_number(number)
        pyperclip.copy(found_contact.email)