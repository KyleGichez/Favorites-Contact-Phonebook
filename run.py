from phonebook import Favorites
def create_contact(fname,lname,phone,email):
    '''
    create a new contact
    '''
    fav_contact = Favorites(fname,lname,phone,email)
    return fav_contact

def save_contacts(contact):
    '''
    save contact
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    delete a contact
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    contact by number
    '''
    return Favorites.find_contact_by_number(number)

def check_existing_contacts(number):
    '''
    check if the contact exists
    '''
    return Favorites.contact_exists(number)

def display_contacts():
    '''
    display all contacts
    '''
    return Favorites.display_contacts()

def main():
    user_name = input("Hi, What is your name?: ")
    print(f"Hello {user_name}. Welcome to your favorites contact list. What would you like to do?")
    print()

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print ("First name: ")
            f_name = input()

            print("Last name: ")
            l_name = input()

            print("Phone number: ")
            p_number = input()

            print("Email address:")
            e_address = input()

            save_contacts(create_contact(f_name, l_name, p_number, e_address)) # create and save new contact.
            print ()
            print(f"New Contact {f_name} {l_name} created")
            print ()

        elif short_code == 'dc':
            if display_contacts():
                print("Here is a list of all your contacts")
                print()

                for contact in display_contacts():
                    print(f"""{contact.first_name} {contact.last_name} {contact.phone_number} {contact.email}""")
                print()
            else:
                print()
                print("You don't seem to have any contacts saved yet!")
                print()

        elif short_code == 'fc':
            print("Enter the number you want to search for: ")

            search_number = str(input()).strip()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f'''{search_contact.first_name} {search_contact.last_name} \n {"-" * 20} ''')
                # print(f"{search_contact.first_name} {search_contact.last_name}")
                # print('-' * 20)
                print(f"Phone number: {search_contact.phone_number}")
                print(f"Email address: {search_contact.email}")
            else:
                print("That contact does not exist!")

        elif short_code == "ex":
            print("Bye! See you next time .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()