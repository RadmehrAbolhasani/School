import sqlite3

# Initialize the database
def initialize_database():
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personal_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        phone TEXT NOT NULL,
        height REAL NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Add personal information to the database
def add_personal_info(name, age, phone, height, email):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO personal_info (name, age, phone, height, email)
    VALUES (?, ?, ?, ?, ?)
    """, (name, age, phone, height, email))
    conn.commit()
    conn.close()
    log_activity(f"Added new person: {name}, {age}, {phone}, {height}, {email}")

# Update personal information with confirmation
def update_personal_info(column, value, name):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal_info WHERE name = ?", (name,))
    result = cursor.fetchone()
    if not result:
        print(f"No record found for {name}.")
        conn.close()
        return

    print(f"Current record for {name}: {result}")
    confirmation = input(f"Are you sure you want to update {column} to '{value}' for {name}? (yes/no): ").lower()
    if confirmation == "yes":
        cursor.execute(f"UPDATE personal_info SET {column} = ? WHERE name = ?", (value, name))
        conn.commit()
        print(f"{column} for {name} has been updated to {value}.")
        log_activity(f"Updated {column} for {name} to {value}")
    else:
        print("Update canceled.")
    conn.close()

# Delete personal information with confirmation
def delete_personal_info(name):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM personal_info WHERE name = ?", (name,))
    result = cursor.fetchone()
    if not result:
        print(f"No record found for {name}.")
        conn.close()
        return

    print(f"Current record for {name}: {result}")
    confirmation = input(f"Are you sure you want to delete the record for {name}? (yes/no): ").lower()
    if confirmation == "yes":
        cursor.execute("DELETE FROM personal_info WHERE name = ?", (name,))
        conn.commit()
        print(f"Record for {name} has been deleted.")
        log_activity(f"Deleted record for {name}")
    else:
        print("Deletion canceled.")
    conn.close()

# Search for a person based on a specific field
def search_person(field, value):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM personal_info WHERE {field} = ?", (value,))
    results = cursor.fetchall()
    conn.close()
    if results:
        for row in results:
            print(row)
        log_activity(f"Searched for {field} = {value}, found {len(results)} result(s).")
    else:
        print(f"No records found for {field} = {value}.")
        log_activity(f"Searched for {field} = {value}, found 0 results.")

# Log activity to a file
def log_activity(activity, filename="activity_log.txt"):
    with open(filename, "a") as file:
        file.write(activity + "\n")

# Main program
if __name__ == "__main__":
    print("Welcome! Let's manage your personal information.")
    print("Type 'exit' to quit the program.")

    initialize_database()

    while True:
        print("\nOptions:")
        print("1. Add a new person")
        print("2. Update existing information")
        print("3. Delete a person")
        print("4. Search for a person")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            # Add a new person
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone number: ")
            height = float(input("Enter height (in cm): "))
            email = input("Enter email: ")
            add_personal_info(name, age, phone, height, email)
            print(f"New person {name} has been added.")

        elif choice == "2":
            # Update existing information
            name = input("Enter the name of the person to update: ")
            column = input("Enter the column to update (age, phone, height, email): ")
            value = input(f"Enter the new value for {column}: ")
            update_personal_info(column, value, name)

        elif choice == "3":
            # Delete a person
            name = input("Enter the name of the person to delete: ")
            delete_personal_info(name)

        elif choice == "4":
            # Search for a person
            field = input("Enter the field to search by (name, age, phone, height, email): ")
            value = input(f"Enter the value to search for in {field}: ")
            search_person(field, value)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
