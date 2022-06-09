import unittest
from contact import Contact

class TestContact(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        test create new contact instance
        """
        self.new_contact = Contact("James", "Muriuki", "07122329112", "james@msn.com")

    def test_init(self):
        """
        test init contact 
        """
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "07122329112")
        self.assertEqual(self.new_contact.email, "james@msn.com")

    def tearDown(self):
        Contact.contact_list = []

    def test_save_contact(self):
        """
        test save contact
        """
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_save_multiple_contacts(self):
        """
        test save multiple contacts
        """
        self.new_contact.save_contact()
        contact1 = Contact("Test", "user", "0712223381","john@65gmail.com")
        contact1.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        """
        test delete contact
        """
        self.new_contact.save_contact()
        contact1 = Contact("Test", "user", "07122383711", "john@65gmail.com")
        contact1.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        """
        test search a contact by number
        """
        self.new_contact.save_contact()
        contact1 = Contact("Test", "user", "07122383711", "john@65gmail.com")
        contact1.save_contact()

        found_contact = Contact.find_by_number("07122383711")
        self.assertEqual(found_contact.email, contact1.email)


if __name__ == '__main__':
    unittest.main()