import re

contacts = []
def valid_name(name):
    return name.replace(" ", "").isalpha()

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def add_contact():
    while True:
        name = input("Enter Name: ")
        if valid_name(name):
            break
        print("Invalid name! Only letters allowed.")

    while True:
        phone = input("Enter Phone Number (10 digits): ")
        if valid_phone(phone):
            break
        print("Invalid phone number!")

    while True:
        email = input("Enter Email: ")
        if valid_email(email):
            break
        print("Invalid email format!")

    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("----------------------------")
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n------- Contact List -------")
    print("----------------------------")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    search = input("Enter name or phone to search: ")

    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\n------- Contact Found -------")
            print("----------------------------")
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            return

    print("Contact not found.\n")


def update_contact():
    name = input("Enter the name of contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():

            while True:
                phone = input("Enter new phone (10 digits): ")
                if valid_phone(phone):
                    contact['phone'] = phone
                    break
                print("Invalid phone number!")

            while True:
                email = input("Enter new email: ")
                if valid_email(email):
                    contact['email'] = email
                    break
                print("Invalid email format!")

            contact['address'] = input("Enter new address: ")

            print("----------------------------")
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    name = input("Enter the name of contact to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("----------------------------")
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


while True:
    print("------- Contact Book -------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("----------------------------")
        print("Exiting program...")
        print("---+++---+++---+++---+++---+++")
        break
    else:
        print("Invalid choice. Try again.\n")