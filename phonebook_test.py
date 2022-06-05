import pyperclip
import unittest
from phonebook import Favorites

class TestFavorites(unittest.TestCase):
    def setUp(self):
        """
        test create a new contact
        """
        self.fav_contact = Favorites("Kyle", "Gichez", "0712230093", "kylegichez@gmail.com")

    def test_init(self):
        """
        test truthiness of the init function
        """
        self.assertEqual(self.fav_contact.first_name, "Kyle")
        self.assertEqual(self.fav_contact.last_name, "Gichez")
        self.assertEqual(self.fav_contact.phone_number, "0712230093")
        self.assertEqual(self.fav_contact.email, "kylegichez@gmail.com")

    def tearDown(self):
        """
        Breaks down and confirms that the length of each contact after saving a contact
        """
        Favorites.favorites_list = []

    def test_save_contact(self):
        """
        test save contact
        """
        self.fav_contact.save_contact()
        self.assertEqual(len(Favorites.favorites_list), 1)

    def test_save_multiple_contacts(self):
        """
        test save multiple contacts
        """
        self.fav_contact.save_contact()
        new_fav_contact = Favorites("Aklisiya", "Eshetu", "0771897561", "aklisiyaeshetu@gmail.com")
        new_fav_contact.save_contact()
        self.assertEqual(len(Favorites.favorites_list), 2)

    def test_delete_contact(self):
        """
        test delete contact
        """
        self.fav_contact.save_contact()
        new_fav_contact = Favorites("Aklisiya", "Eshetu", "0771897561", "aklisiyaeshetu@gmail.com")
        new_fav_contact.save_contact()
        new_fav_contact.delete_contact()
        self.assertEqual(len(Favorites.favorites_list), 1)

    def test_find_contact(self):
        """
        test find contact by number
        """
        self.fav_contact.save_contact()
        new_fav_contact = Favorites("Aklisiya", "Eshetu", "0771897561", "aklisiyaeshetu@gmail.com")
        new_fav_contact.save_contact()

        find_contact = Favorites.find_contact_by_number("0771897561")
        self.assertEqual(find_contact.email, new_fav_contact.email)

    def test_check_contact_existence(self):
        """
        test check if contact exists
        """
        self.fav_contact.save_contact()
        new_fav_contact = Favorites("Aklisiya", "Eshetu", "0771897561", "aklisiyaeshetu@gmail.com")
        new_fav_contact.save_contact()

        check_contact = Favorites.contact_exists("0712230093")
        self.assertTrue(check_contact)

    def test_display_contacts(self):
        """
        test display all contacts
        """
        self.assertEqual(Favorites.display_contacts(), Favorites.favorites_list)

    def test_copy_email(self):
        """
        test copy email adress
        """
        self.fav_contact.save_contact()
        Favorites.copy_email("0712230093")
        self.assertEqual(self.fav_contact.email, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()