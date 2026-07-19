contacts = {}


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    print("\n✅ Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n----- Contact List -----")
    for name, details in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {details['Phone']}")
        print("-" * 25)


def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print("\nContact Found")
        print(f"Name    : {name}")
        print(f"Phone   : {contacts[name]['Phone']}")
        print(f"Email   : {contacts[name]['Email']}")
        print(f"Address : {contacts[name]['Address']}\n")
    else:
        print("\nContact not found.\n")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        contacts[name]["Address"] = input("New Address: ")

        print("\n✅ Contact updated successfully!\n")
    else:
        print("\nContact not found.\n")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("\n✅ Contact deleted successfully!\n")
    else:
        print("\nContact not found.\n")


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

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
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\nInvalid choice. Try again.\n")