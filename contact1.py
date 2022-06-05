class Contact1:
    contact_list1 = []
    def __init__ (self, first_name, last_name, phone_number, email):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):
        """
        """
        contact_list = self.contact_list1
        contact_list.append(self)
        return self in contact_list