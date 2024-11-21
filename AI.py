# person_details_ai.py

class PersonDetailsAI:
    def __init__(self):
        """Initialize the AI with an empty dictionary to store person details."""
        self.person_data = {}

    def add_person(self, person_id, details):
        """Add a new person's details."""
        if person_id in self.person_data:
            print(f"Error: Person with ID {person_id} already exists.")
        else:
            self.person_data[person_id] = details
            print(f"Person with ID {person_id} added successfully.")

    def view_person(self, person_id):
        """View details of a person by ID."""
        details = self.person_data.get(person_id)
        if details:
            print(f"Details for ID {person_id}: {details}")
        else:
            print(f"No person found with ID {person_id}.")

    def update_person(self, person_id, updated_details):
        """Update details of an existing person."""
        if person_id in self.person_data:
            self.person_data[person_id].update(updated_details)
            print(f"Details for ID {person_id} updated successfully.")
        else:
            print(f"No person found with ID {person_id}.")

    def delete_person(self, person_id):
        """Delete a person's details."""
        if person_id in self.person_data:
            del self.person_data[person_id]
            print(f"Person with ID {person_id} deleted successfully.")
        else:
            print(f"No person found with ID {person_id}.")

    def search_person_by_name(self, name):
        """Search for people by name."""
        results = {pid: details for pid, details in self.person_data.items() if details.get("name") == name}
        if results:
            print(f"People with name '{name}': {results}")
        else:
            print(f"No person found with name '{name}'.")

    def show_all(self):
        """Display all stored person details."""
        if self.person_data:
            print("All stored person details:")
            for person_id, details in self.person_data.items():
                print(f"ID: {person_id}, Details: {details}")
        else:
            print("No person details stored yet.")

def main():
    ai = PersonDetailsAI()
    while True:
        print("\nPerson Details AI Menu:")
        print("1. Add Person")
        print("2. View Person")
        print("3. Update Person")
        print("4. Delete Person")
        print("5. Search by Name")
        print("6. Show All")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            person_id = input("Enter person ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            details = {"name": name, "age": age, "email": email}
            ai.add_person(person_id, details)

        elif choice == "2":
            person_id = input("Enter person ID to view: ")
            ai.view_person(person_id)

        elif choice == "3":
            person_id = input("Enter person ID to update: ")
            print("Enter updated details (leave blank to keep current values):")
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            updated_details = {}
            if name:
                updated_details["name"] = name
            if age:
                updated_details["age"] = age
            if email:
                updated_details["email"] = email
            ai.update_person(person_id, updated_details)

        elif choice == "4":
            person_id = input("Enter person ID to delete: ")
            ai.delete_person(person_id)

        elif choice == "5":
            name = input("Enter name to search: ")
            ai.search_person_by_name(name)

        elif choice == "6":
            ai.show_all()

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
