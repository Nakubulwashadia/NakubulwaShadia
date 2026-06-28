# student_management.py
# Student Record Management System

import csv
import json
import logging
import os

# -------------------- Logging Setup --------------------
logging.basicConfig(
    filename='student_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CSV_FILE = 'students.csv'
JSON_FILE = 'students.json'


# -------------------- Custom Exception --------------------
class StudentNotFoundException(Exception):
    pass


# -------------------- Helper Functions --------------------
def initialize_files():
    """Create files if they don't exist"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['RegNo', 'Name', 'Age'])

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as file:
            json.dump({}, file)


def load_json():
    with open(JSON_FILE, 'r') as file:
        return json.load(file)


def save_json(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)


# -------------------- Core Functions --------------------
def add_student():
    try:
        reg = input("Enter Registration Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        if not age.isdigit():
            raise ValueError("Age must be a number")

        address = input("Enter Address: ")
        contact = input("Enter Contact: ")
        program = input("Enter Program: ")

        # Save to CSV
        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([reg, name, age])

        # Save to JSON
        data = load_json()
        data[reg] = {
            "address": address,
            "contact": contact,
            "program": program
        }
        save_json(data)

        logging.info(f"Added student {reg}")
        print("Student added successfully!")

    except Exception as e:
        logging.error(f"Error adding student: {e}")
        print("Error:", e)


def view_students():
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

        logging.info("Viewed all students")

    except Exception as e:
        logging.error(f"Error viewing students: {e}")
        print("Error:", e)


def search_student():
    try:
        reg = input("Enter Registration Number: ")
        found = False

        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == reg:
                    print("Student Found:", row)
                    found = True

        data = load_json()
        if reg in data:
            print("Additional Info:", data[reg])

        if not found:
            raise StudentNotFoundException("Student not found")

        logging.info(f"Searched student {reg}")

    except StudentNotFoundException as e:
        logging.warning(e)
        print(e)

    except Exception as e:
        logging.error(f"Error searching student: {e}")
        print("Error:", e)


def update_student():
    try:
        reg = input("Enter Registration Number to update: ")
        rows = []
        found = False

        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == reg:
                    found = True
                    row[1] = input("Enter new name: ")
                    row[2] = input("Enter new age: ")
                rows.append(row)

        if not found:
            raise StudentNotFoundException("Student not found")

        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        data = load_json()
        if reg in data:
            data[reg]["address"] = input("New address: ")
            data[reg]["contact"] = input("New contact: ")
            data[reg]["program"] = input("New program: ")
            save_json(data)

        logging.info(f"Updated student {reg}")
        print("Student updated successfully!")

    except StudentNotFoundException as e:
        logging.warning(e)
        print(e)

    except Exception as e:
        logging.error(f"Error updating student: {e}")
        print("Error:", e)


def delete_student():
    try:
        reg = input("Enter Registration Number to delete: ")
        rows = []
        found = False

        with open(CSV_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != reg:
                    rows.append(row)
                else:
                    found = True

        if not found:
            raise StudentNotFoundException("Student not found")

        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        data = load_json()
        if reg in data:
            del data[reg]
            save_json(data)

        logging.info(f"Deleted student {reg}")
        print("Student deleted successfully!")

    except StudentNotFoundException as e:
        logging.warning(e)
        print(e)

    except Exception as e:
        logging.error(f"Error deleting student: {e}")
        print("Error:", e)


# -------------------- Menu --------------------
def menu():
    initialize_files()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
