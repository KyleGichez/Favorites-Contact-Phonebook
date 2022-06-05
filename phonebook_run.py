from phonebook import Favorites

def create_contact(first_name, last_name, phone_number, email):
    """
    create a new fav contact
    """
    fav_contact = Favorites(first_name, last_name, phone_number, email)
    return fav_contact

def save_contact(contact):
    """
    save fav contact
    """
    contact.save_contact()

def delete_contact(contact):
    """
    delete fav contact
    """
    contact.delete_contact()

def find_contact_by_number(number):
    """
    find contact by number
    """
    return Favorites.find_contact_by_number(number)

def check_if_exists(number):
    """
    check if number exists
    """
    return Favorites.check_if_exists(number)

def display_contacts(contacts):
    """
    display all contacts
    """
    return Favorites.display_contacts(contacts)
