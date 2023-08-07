import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact for {name} added successfully.")

def search_contact(contacts, name):
    if name in contacts:
        contact_info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
    else:
        print(f"Contact with name '{name}' not found.")

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        save_contacts(contacts)
        print(f"Contact for {name} updated successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully.")
    else:
        print(f"Contact with name '{name}' not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("------------------------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)
        
        elif choice == "2":
            name = input("Enter contact name: ")
            search_contact(contacts, name)
        
        elif choice == "3":
            name = input("Enter contact name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            update_contact(contacts, name, phone, email)
        
        elif choice == "4":
            name = input("Enter contact name: ")
            delete_contact(contacts, name)
        
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
