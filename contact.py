class Contact:
    """
    contact list
    """
    contact_list = []
    def __init__ (self, first_name, last_name, phone_number, email):
        """
        init contact
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    
    def save_contact(self):
        """
        save contact
        """
        self.contact_list.append(self)

    def delete_contact(self):
        """
        delete a saved contact
        """
        self.contact_list.remove(self)

    def display_contacts(self):
        """
        display all contacts
        """
        return self.contact_list(self)
    
    @classmethod
    def find_by_number(cls, number):
        """
        find a contact by searching the phone number
        return contact if it exists
        """
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact


