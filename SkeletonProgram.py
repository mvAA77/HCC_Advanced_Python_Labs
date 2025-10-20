"""
Contact Book Application
Console Version Skeleton Program
Prepared for Checkpoint 2 Assignment
CMSY 257 - Howard Community College
"""

import sqlite3
from datetime import datetime

class Contact:
    """Class to represent a single contact"""
    
    def __init__(self, name="", phone="", email="", address=""):
        """
        Initialize a contact with basic information
        
        Args:
            name (str): Contact's full name
            phone (str): Contact's phone number
            email (str): Contact's email address
            address (str): Contact's physical address
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def display_contact(self):
        """Display contact information in a formatted way"""
        print(f"\nName: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Created: {self.created_date}")
        print("-" * 30)
    
    def to_dict(self):
        """
        Convert contact to dictionary for database operations
        
        Returns:
            dict: Contact data as dictionary
        """
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'created_date': self.created_date
        }


class ContactBook:
    """Main class to manage the contact book operations"""
    
    def __init__(self, db_name="contacts.db"):
        """
        Initialize the contact book with database connection
        
        Args:
            db_name (str): Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.initialize_database()
    
    def initialize_database(self):
        """Initialize the SQLite database and create contacts table if it doesn't exist"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            
            # Create contacts table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT,
                    email TEXT,
                    address TEXT,
                    created_date TEXT
                )
            ''')
            self.connection.commit()
            print("Contact database initialized successfully!")
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def add_contact(self, contact):
        """
        Add a new contact to the database
        
        Args:
            contact (Contact): Contact object to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
                INSERT INTO contacts (name, phone, email, address, created_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (contact.name, contact.phone, contact.email, contact.address, contact.created_date))
            
            self.connection.commit()
            print(f"Contact '{contact.name}' added successfully!")
            return True
            
        except sqlite3.Error as e:
            print(f"Error adding contact: {e}")
            return False
    
    def search_contacts(self, search_term):
        """
        Search for contacts by name, phone, or email
        
        Args:
            search_term (str): Term to search for
            
        Returns:
            list: List of Contact objects matching the search
        """
        try:
            self.cursor.execute('''
                SELECT * FROM contacts 
                WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            
            results = self.cursor.fetchall()
            contacts = []
            
            for row in results:
                contact = Contact()
                contact.name = row[1]
                contact.phone = row[2]
                contact.email = row[3]
                contact.address = row[4]
                contact.created_date = row[5]
                contacts.append(contact)
            
            return contacts
            
        except sqlite3.Error as e:
            print(f"Error searching contacts: {e}")
            return []
    
    def get_all_contacts(self):
        """
        Retrieve all contacts from the database
        
        Returns:
            list: List of all Contact objects
        """
        try:
            self.cursor.execute('SELECT * FROM contacts ORDER BY name')
            results = self.cursor.fetchall()
            contacts = []
            
            for row in results:
                contact = Contact()
                contact.name = row[1]
                contact.phone = row[2]
                contact.email = row[3]
                contact.address = row[4]
                contact.created_date = row[5]
                contacts.append(contact)
            
            return contacts
            
        except sqlite3.Error as e:
            print(f"Error retrieving contacts: {e}")
            return []
    
    def update_contact(self, old_name, updated_contact):
        """
        Update an existing contact
        
        Args:
            old_name (str): Original name of the contact to update
            updated_contact (Contact): Updated contact information
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('''
                UPDATE contacts 
                SET name=?, phone=?, email=?, address=?
                WHERE name=?
            ''', (updated_contact.name, updated_contact.phone, updated_contact.email, 
                  updated_contact.address, old_name))
            
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"Contact '{old_name}' updated successfully!")
                return True
            else:
                print(f"Contact '{old_name}' not found!")
                return False
            
        except sqlite3.Error as e:
            print(f"Error updating contact: {e}")
            return False
    
    def delete_contact(self, name):
        """
        Delete a contact by name
        
        Args:
            name (str): Name of the contact to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.cursor.execute('DELETE FROM contacts WHERE name=?', (name,))
            self.connection.commit()
            
            if self.cursor.rowcount > 0:
                print(f"Contact '{name}' deleted successfully!")
                return True
            else:
                print(f"Contact '{name}' not found!")
                return False
                
        except sqlite3.Error as e:
            print(f"Error deleting contact: {e}")
            return False
    
    def count_contacts(self):
        """
        Count the total number of contacts in the database
        
        Returns:
            int: Number of contacts
        """
        try:
            self.cursor.execute('SELECT COUNT(*) FROM contacts')
            count = self.cursor.fetchone()[0]
            return count
        except sqlite3.Error as e:
            print(f"Error counting contacts: {e}")
            return 0
    
    def close_connection(self):
        """Close the database connection"""
        if self.connection:
            self.connection.close()


class ContactBookApp:
    """Application class to handle user interface and menu operations"""
    
    def __init__(self):
        """Initialize the contact book application"""
        self.contact_book = ContactBook()
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "=" * 40)
        print("        CONTACT BOOK APPLICATION")
        print("=" * 40)
        print("1. Add New Contact")
        print("2. Search Contacts")
        print("3. View All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Count Contacts")
        print("7. Exit")
        print("=" * 40)
    
    def get_contact_input(self):
        """
        Get contact information from user input
        
        Returns:
            Contact: Contact object with user input
        """
        print("\nEnter Contact Details:")
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        
        # Validate required name field
        if not name:
            print("Error: Name is required!")
            return None
            
        return Contact(name, phone, email, address)
    
    def add_contact_flow(self):
        """Handle the add contact user flow"""
        print("\n--- Add New Contact ---")
        contact = self.get_contact_input()
        if contact:
            self.contact_book.add_contact(contact)
    
    def search_contacts_flow(self):
        """Handle the search contacts user flow"""
        print("\n--- Search Contacts ---")
        search_term = input("Enter search term (name, phone, or email): ").strip()
        
        if search_term:
            results = self.contact_book.search_contacts(search_term)
            if results:
                print(f"\nFound {len(results)} matching contact(s):")
                for contact in results:
                    contact.display_contact()
            else:
                print("No contacts found matching your search.")
        else:
            print("Please enter a search term.")
    
    def view_all_contacts_flow(self):
        """Handle the view all contacts user flow"""
        print("\n--- All Contacts ---")
        contacts = self.contact_book.get_all_contacts()
        
        if contacts:
            print(f"Total contacts: {len(contacts)}")
            for contact in contacts:
                contact.display_contact()
        else:
            print("No contacts found in the database.")
    
    def update_contact_flow(self):
        """Handle the update contact user flow"""
        print("\n--- Update Contact ---")
        old_name = input("Enter the name of the contact to update: ").strip()
        
        if not old_name:
            print("Please enter a contact name.")
            return
        
        # Check if contact exists
        existing_contacts = self.contact_book.search_contacts(old_name)
        if not existing_contacts:
            print(f"Contact '{old_name}' not found!")
            return
        
        print(f"\nUpdating contact: {old_name}")
        print("Enter new details:")
        
        # Get updated information
        updated_contact = self.get_contact_input()
        if updated_contact:
            self.contact_book.update_contact(old_name, updated_contact)
    
    def delete_contact_flow(self):
        """Handle the delete contact user flow"""
        print("\n--- Delete Contact ---")
        name = input("Enter the name of the contact to delete: ").strip()
        
        if name:
            self.contact_book.delete_contact(name)
        else:
            print("Please enter a contact name.")
    
    def count_contacts_flow(self):
        """Handle the count contacts user flow"""
        count = self.contact_book.count_contacts()
        print(f"\nTotal contacts in database: {count}")
    
    def run(self):
        """Main method to run the contact book application"""
        print("Welcome to the Contact Book Application!")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                self.add_contact_flow()
            elif choice == '2':
                self.search_contacts_flow()
            elif choice == '3':
                self.view_all_contacts_flow()
            elif choice == '4':
                self.update_contact_flow()
            elif choice == '5':
                self.delete_contact_flow()
            elif choice == '6':
                self.count_contacts_flow()
            elif choice == '7':
                print("Thank you for using the Contact Book Application!")
                self.contact_book.close_connection()
                break
            else:
                print("Invalid choice! Please enter a number between 1-7.")


def test_contact_functionality():
    """Test function to demonstrate the contact book functionality"""
    print("TESTING CONTACT BOOK FUNCTIONALITY")
    print("=" * 40)
    
    # Create a test contact book
    test_book = ContactBook("test_contacts.db")
    
    # Test Contact class
    print("\n1. Testing Contact Class:")
    test_contact = Contact("John Doe", "123-456-7890", "john@email.com", "123 Main St")
    test_contact.display_contact()
    
    # Test adding contact
    print("\n2. Testing Add Contact:")
    test_book.add_contact(test_contact)
    
    # Test counting contacts
    print("\n3. Testing Contact Count:")
    count = test_book.count_contacts()
    print(f"Contacts in database: {count}")
    
    # Test searching contacts
    print("\n4. Testing Search Function:")
    results = test_book.search_contacts("John")
    print(f"Search results for 'John': {len(results)} contacts found")
    for contact in results:
        contact.display_contact()
    
    # Test getting all contacts
    print("\n5. Testing Get All Contacts:")
    all_contacts = test_book.get_all_contacts()
    print(f"All contacts retrieved: {len(all_contacts)}")
    
    # Test updating contact
    print("\n6. Testing Update Contact:")
    updated_contact = Contact("John Smith", "123-456-7890", "john.smith@email.com", "456 Oak Ave")
    test_book.update_contact("John Doe", updated_contact)
    
    # Verify update worked
    updated_results = test_book.search_contacts("John Smith")
    print(f"After update - contacts found: {len(updated_results)}")
    
    # Test deleting contact
    print("\n7. Testing Delete Contact:")
    test_book.delete_contact("John Smith")
    
    # Verify delete worked
    final_count = test_book.count_contacts()
    print(f"Final contact count: {final_count}")
    
    # Clean up test database
    test_book.close_connection()
    import os
    if os.path.exists("test_contacts.db"):
        os.remove("test_contacts.db")
        print("\nTest database cleaned up.")
    
    print("\nAll tests completed successfully!")


def main():
    """Main function to run the program"""
    # Run test functionality
    test_contact_functionality()
    
    print("\n" + "=" * 50)
    print("STARTING CONTACT BOOK APPLICATION")
    print("=" * 50)
    
    # Create and run the actual application
    app = ContactBookApp()
    app.run()


if __name__ == "__main__":
    main()