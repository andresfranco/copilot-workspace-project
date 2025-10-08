import sys

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                add_contact(name, phone)
            elif choice == '2':
                name = input("Enter name to view: ")
                view_contact(name)
            elif choice == '3':
                name = input("Enter name to delete: ")
                delete_contact(name)
            elif choice == '4':
                names = list_all_contacts()
                if names:
                    print("All contacts:")
                    for n in names:
                        print(n)
                else:
                    print("No contacts found.")
            elif choice == '5':
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid option. Try again.")

    def list_all_contacts():
        """Return a list of all contact names in the contact book."""
        return list(contacts.keys())
if __name__ == "__main__":
    main()
