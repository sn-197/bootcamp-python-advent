# Create a contacts list using a list of dictionaries. 
# Each dictionary represents a contact with keys for "name", "phone", and "email".

contacts = {
    1: {"contact_id": 13243, "name": "Justine Balcony", "phone": "010-4567890", "email": "justine.balcony@test.com"},
    2: {"contact_id": 26768, "name": "Billy Bob Hall", "phone": "020-9876540", "email": "billy.bob.hall@test.com"},
    3: {"contact_id": 3243143, "name": "Charlie Brown", "phone": "030-1234567", "email": "charlie.brown@test.com"},
}

# After asking for Dark Roast Style review
# Improve this significantly by using a class to represent each contact instead of a dictionary.

from dataclasses import dataclass

@dataclass
class Contact:
    contact_id: int
    name: str
    phone: str
    email: str

contacts = {
    "Justine Balcony": Contact(contact_id=13243, name="Justine Balcony", phone="010-4567890", email="justine.balcony@test.com"),
    "Billy Bob Hall": Contact(contact_id=26768, name="Billy Bob Hall", phone="020-9876540", email="billy.bob.hall@test.com"),
    "Charlie Brown": Contact(contact_id=3243143, name="Charlie Brown", phone="030-1234567", email="charlie.brown@test.com"),
}

print(contacts["Justine Balcony"].email)