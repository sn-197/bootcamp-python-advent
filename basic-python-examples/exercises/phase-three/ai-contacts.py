import json
import os


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
        else:
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, contact_id, name, phone, email):
        if contact_id in self.contacts:
            print("⚠ Contact ID already exists.")
            return
        self.contacts[contact_id] = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.save_contacts()
        print("✅ Contact added successfully.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for cid, info in self.contacts.items():
            print(f"\nID: {cid}")
            print(f"Name: {info['name']}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")

    def find_contact(self, contact_id):
        contact = self.contacts.get(contact_id)
        if contact:
            print(f"\nID: {contact_id}")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("❌ Contact not found.")

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            self.save_contacts()
            print("🗑 Contact deleted.")
        else:
            print("❌ Contact not found.")


def main():
    book = ContactBook()

    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Find Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            cid = input("Enter Contact ID: ")
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            book.add_contact(cid, name, phone, email)

        elif choice == "2":
            book.list_contacts()

        elif choice == "3":
            cid = input("Enter Contact ID to search: ")
            book.find_contact(cid)

        elif choice == "4":
            cid = input("Enter Contact ID to delete: ")
            book.delete_contact(cid)

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()