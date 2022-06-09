from phonebook import Favorites

def create_contact(first_name, last_name, phone_number, email):
    """create a new fav contact"""
    fav_contact = Favorites(first_name, last_name, phone_number, email)
    return fav_contact

def save_contact(contact):
    """save fav contact"""
    contact.save_contact()

def delete_contact(contact):
    """delete fav contact"""
    contact.delete_contact(contact)

def find_contact_by_number(number):
    """find contact by number"""
    return Favorites.find_contact_by_number(number)

def check_if_exists(number):
    """check if number exists"""
    return Favorites.contact_exists(number)

def display_contacts():
    """display all contacts"""
    return Favorites.display_contacts()

def main():
    username = input("Enter your username: ")
    print()
    print(f"Hello {username}, how are you doing today? Welcome to your favorites contact phonebook.....what would you love to do with your contact phonebook?")
    print()

    while True:
        print()
        print(f"Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == "cc":
            f_name = input("First name....")
            l_name = input("Last name.... ")
            p_number = input("Phone number....")
            e_address = input("Email address....")

            save_contact(create_contact(f_name, l_name, p_number, e_address))
            print()
            print(f"New favorite contact {f_name} {l_name} successfuly created.")
            print()

        elif short_code == "dc":
            if display_contacts():
                print("Look!, here is a list of all your favorite contacts....")
                print()
                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name}....   {contact.phone_number}....   {contact.email}")
                print()
            else:
                print("Ooopss!! You don't seem to have any saved contacts in your phonebook.")

        elif short_code == "fc":
            number = input("Please enter the number you want to search for: ")

            if find_contact_by_number(number):
                search_number = find_contact_by_number(number)
                print(f'''Name:{search_number.first_name} {search_number.last_name}  {"." * 7}  {search_number.phone_number} {"." * 7}  {search_number.email}''')
                print()
            else:
                print("That number doesn't exist!!")

        elif short_code == "ex":
            print(f"Bye {username} !! See you next time....")
            break
        
        else:
            print("I didn't get that quite well, please use the short codes for your phonebook navigation.")


if __name__ == '__main__':
    main()
