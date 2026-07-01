# Assignment: Function-based Contact Management System
import re

class ContactManager:
    def __init__(self):
        self.contacts = {}

    # ============================================
    #         TASK 1: DATA VALIDATION HELPERS
    # ============================================

    def validate_phone(self, phone):
        """Phone must contain only digits and hyphens e.g +256-701-123456"""
        for char in phone:
            if not (char.isdigit() or char == '-' or char == '+'):
                return False
        return True

    def validate_email(self, email):
        """Email must contain @ and a period"""
        if email == "":
            return True  # email is optional
        if "@" in email and "." in email:
            return True
        return False

    # ============================================
    #              CRUD OPERATIONS
    # ============================================

    def add_contact(self, name, phone, email="", address=""):
        """Add a new contact"""
        # Validate phone
        if not self.validate_phone(phone):
            print("❌ Invalid phone number! Use only digits, hyphens and + (e.g. +256-701-123456)")
            return

        # Validate email
        if not self.validate_email(email):
            print("❌ Invalid email! Must contain '@' and '.' (e.g. name@gmail.com)")
            return

        if name in self.contacts:
            print(f"❌ Contact '{name}' already exists!")
            return

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"✅ Contact '{name}' added successfully!")

    def view_contact(self, name):
        """View a single contact"""
        if name not in self.contacts:
            print(f"❌ Contact '{name}' not found!")
            return

        contact = self.contacts[name]
        print(f"""
╔══════════════════════════════════╗
           CONTACT DETAILS
╚══════════════════════════════════╝
  Name    : {name}
  Phone   : {contact['phone']}
  Email   : {contact['email'] if contact['email'] else 'N/A'}
  Address : {contact['address'] if contact['address'] else 'N/A'}
{"=" * 36}""")

    def update_contact(self, name, phone=None, email=None, address=None):
        """Update an existing contact"""
        if name not in self.contacts:
            print(f"❌ Contact '{name}' not found!")
            return

        # Validate phone if provided
        if phone:
            if not self.validate_phone(phone):
                print("❌ Invalid phone number! Use only digits, hyphens and + (e.g. +256-701-123456)")
                return
            self.contacts[name]["phone"] = phone

        # Validate email if provided
        if email:
            if not self.validate_email(email):
                print("❌ Invalid email! Must contain '@' and '.' (e.g. name@gmail.com)")
                return
            self.contacts[name]["email"] = email

        if address:
            self.contacts[name]["address"] = address

        print(f"✅ Contact '{name}' updated successfully!")

    def delete_contact(self, name):
        """Delete a contact"""
        if name not in self.contacts:
            print(f"❌ Contact '{name}' not found!")
            return

        del self.contacts[name]
        print(f"✅ Contact '{name}' deleted successfully!")

    def list_all_contacts(self):
        """List all contacts"""
        if not self.contacts:
            print("❌ No contacts found!")
            return

        print(f"""
╔══════════════════════════════════════════════════════════╗
                     ALL CONTACTS
╚══════════════════════════════════════════════════════════╝""")
        print(f"  {'No.':<5} {'Name':<20} {'Phone':<20} {'Email'}")
        print("  " + "-" * 60)

        for i, (name, details) in enumerate(self.contacts.items(), 1):
            email = details['email'] if details['email'] else 'N/A'
            print(f"  {i:<5} {name:<20} {details['phone']:<20} {email}")
        print("=" * 62)
        print(f"  Total contacts: {len(self.contacts)}")

    # ============================================
    #         TASK 2: ADVANCED SEARCH
    # ============================================

    def search_contacts(self, query):
        """Search contacts by name, phone or email"""
        query = query.lower()
        results = []

        for name, details in self.contacts.items():
            if (query in name.lower() or
                query in details['phone'] or
                query in details['email'].lower()):
                results.append((name, details))

        # Display results in clean format
        if not results:
            print(f"\n❌ No contacts found matching '{query}'")
            return

        print(f"""
╔══════════════════════════════════════════════════════════╗
          SEARCH RESULTS FOR '{query.upper()}'
╚══════════════════════════════════════════════════════════╝""")
        print(f"  {'No.':<5} {'Name':<20} {'Phone':<20} {'Email'}")
        print("  " + "-" * 60)

        for i, (name, details) in enumerate(results, 1):
            email = details['email'] if details['email'] else 'N/A'
            print(f"  {i:<5} {name:<20} {details['phone']:<20} {email}")

        print("=" * 62)
        print(f"  {len(results)} result(s) found.")


# ============================================
#       TASK 3: INTERACTIVE CLI MENU
# ============================================

def main():
    manager = ContactManager()

    # Add some sample contacts to start with
    manager.add_contact("Shadia", "+256-701-123456", "shadia@gmail.com", "Kampala")
    manager.add_contact("Rinah", "+256-782-654321", "rinah@gmail.com", "Entebbe")
    manager.add_contact("Brian", "+256-756-987654", "brian@gmail.com", "Jinja")

    while True:
        print("""
=== Contact Manager Menu === 
1. Add Contact
2. View Contact
3. Update Contact
4. Delete Contact
5. Search Contacts
6. List All Contacts
7. Exit

Choose an option (1-7): """, end="")

        choice = input().strip()

        # ---- ADD CONTACT ----
        if choice == "1":
            print("\n--- Add Contact ---")
            name    = input("Enter name: ").strip()
            phone   = input("Enter phone (e.g. +256-701-123456): ").strip()
            email   = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            manager.add_contact(name, phone, email, address)

        # ---- VIEW CONTACT ----
        elif choice == "2":
            print("\n--- View Contact ---")
            name = input("Enter name to view: ").strip()
            manager.view_contact(name)

        # ---- UPDATE CONTACT ----
        elif choice == "3":
            print("\n--- Update Contact ---")
            name    = input("Enter name to update: ").strip()
            phone   = input("New phone (press Enter to skip): ").strip()
            email   = input("New email (press Enter to skip): ").strip()
            address = input("New address (press Enter to skip): ").strip()
            manager.update_contact(
                name,
                phone   if phone   else None,
                email   if email   else None,
                address if address else None
            )

        # ---- DELETE CONTACT ----
        elif choice == "4":
            print("\n--- Delete Contact ---")
            name = input("Enter name to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                manager.delete_contact(name)
            else:
                print("❌ Delete cancelled.")

        # ---- SEARCH CONTACTS ----
        elif choice == "5":
            print("\n--- Search Contacts ---")
            query = input("Enter name, phone or email to search: ").strip()
            manager.search_contacts(query)

        # ---- LIST ALL CONTACTS ----
        elif choice == "6":
            manager.list_all_contacts()

        # ---- EXIT ----
        elif choice == "7":
            print("\n👋 Goodbye! Have a great day!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 7.")

# Run the program
main()