import json

class ContactManager:
    def __init__(self):
        self.contacts = []  # Bad practice: Using a list instead of a more structured format

    def add_contact(self, name, email, phone):
        # Bad practice: No validation for email format or phone number
        contact = {
            'name': name,
            'email': email,
            'phone': phone
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        # Bad practice: No error handling if the contact does not exist
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found!")  # Bad practice: Should use exceptions instead

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")  # Bad practice: Should handle this in a more user-friendly way
            return
        
        print("Contacts List:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

    def save_contacts_to_file(self, file_path):
        with open(file_path, 'w') as f:  # Bad practice: No error handling for file I/O
            json.dump(self.contacts, f)
            print(f"Contacts saved to {file_path}.")

    def load_contacts_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:  # Bad practice: No error handling for file I/O
                self.contacts = json.load(f)
                print(f"Contacts loaded from {file_path}.")
        except FileNotFoundError:
            print("File not found. No contacts loaded.")  # Bad practice: Should handle this properly


# Example usage
if __name__ == "__main__":
    manager = ContactManager()
    
    # Bad practice: Hardcoding values; should take input from the user or a config file
    manager.add_contact("Alice Johnson", "alice@example.com", "123-456-7890")
    manager.add_contact("Bob Smith", "bob@example.com", "098-765-4321")
    
    manager.list_contacts()

    # Bad practice: No validation for deletion
    manager.delete_contact("Alice Johnson")
    manager.delete_contact("Charlie Brown")  # Contact not found

    manager.list_contacts()

    # Bad practice: No cleanup or confirmation for saving/loading
    manager.save_contacts_to_file("contacts.json")
    manager.load_contacts_from_file("contacts.json")
