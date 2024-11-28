# person_details_manager.py

import sqlite3


class PersonDatabase:
    """Handles all database operations for person details."""

    def __init__(self, db_name="person_details.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create the persons table if it doesn't already exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        self.connection.commit()

    def add_person(self, name, age, email):
        """Add a new person to the database."""
        try:
            self.cursor.execute("INSERT INTO persons (name, age, email) VALUES (?, ?, ?)", (name, age, email))
            self.connection.commit()
            print("Person added successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email already exists in the database.")

    def view_person(self, person_id):
        """Retrieve details of a person by ID."""
        self.cursor.execute("SELECT * FROM persons WHERE id = ?", (person_id,))
        result = self.cursor.fetchone()
        if result:
            print(f"ID: {result[0]}, Name: {result[1]}, Age: {result[2]}, Email: {result[3]}")
        else:
            print("No person found with the given ID.")

    def update_person(self, person_id, name=None, age=None, email=None):
        """Update details of an existing person."""
        existing_person = self.cursor.execute("SELECT * FROM persons WHERE id = ?", (person_id,)).fetchone()
        if not existing_person:
            print("Error: No person found with the given ID.")
            return

        # Use existing values if no update is provided
        updated_name = name if name else existing_person[1]
        updated_age = age if age else existing_person[2]
        updated_email = email if email else existing_person[3]

        try:
            self.cursor.execute("""
                UPDATE persons
                SET name = ?, age = ?, email = ?
                WHERE id = ?
            """, (updated_name, updated_age, updated_email, person_id))
            self.connection.commit()
            print("Person details updated successfully.")
        except sqlite3.IntegrityError:
            print("Error: Email already exists in the database.")

    def delete_person(self, person_id):
        """Delete a person from the database."""
        self.cursor.execute("DELETE FROM persons WHERE id = ?", (person_id,))
        if self.cursor.rowcount > 0:
            self.connection.commit()
            print("Person deleted successfully.")
        else:
            print("Error: No person found with the given ID.")

    def search_person(self, name=None, age=None, email=None):
        """Search for people by name, age, or email."""
        query = "SELECT * FROM persons WHERE 1=1"
        params = []

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")
        if age:
            query += " AND age = ?"
            params.append(age)
        if email:
            query += " AND email LIKE ?"
            params.append(f"%{email}%")

        self.cursor.execute(query, tuple(params))
        results = self.cursor.fetchall()

        if results:
            for person in results:
                print(f"ID: {person[0]}, Name: {person[1]}, Age: {person[2]}, Email: {person[3]}")
        else:
            print("No matching persons found.")

    def show_all(self):
        """Display all persons in the database."""
        self.cursor.execute("SELECT * FROM persons")
        results = self.cursor.fetchall()

        if results:
            for person in results:
                print(f"ID: {person[0]}, Name: {person[1]}, Age: {person[2]}, Email: {person[3]}")
        else:
            print("No persons found in the database.")

    def close(self):
        """Close the database connection."""
        self.connection.close()


def main():
    db = PersonDatabase()

    while True:
        print("\nPerson Details Manager Menu:")
        print("1. Add Person")
        print("2. View Person")
        print("3. Update Person")
        print("4. Delete Person")
        print("5. Search Person")
        print("6. Show All")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            db.add_person(name, age, email)

        elif choice == "2":
            person_id = int(input("Enter person ID: "))
            db.view_person(person_id)

        elif choice == "3":
            person_id = int(input("Enter person ID to update: "))
            print("Enter updated details (leave blank to keep current values):")
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")

            updated_age = int(age) if age else None
            db.update_person(person_id, name=name, age=updated_age, email=email)

        elif choice == "4":
            person_id = int(input("Enter person ID to delete: "))
            db.delete_person(person_id)

        elif choice == "5":
            print("Enter search criteria (leave blank to skip):")
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")

            search_age = int(age) if age else None
            db.search_person(name=name, age=search_age, email=email)

        elif choice == "6":
            db.show_all()

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            db.close()
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
