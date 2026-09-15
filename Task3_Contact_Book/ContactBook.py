contacts = []

while True:
    print("================================")
    print("        CONTACT BOOK")
    print("================================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found!")
        else:
            print("----- Contact List -----")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

    elif choice == "3":
        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("Contact found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)

                print("Contact deleted successfully!")

                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")