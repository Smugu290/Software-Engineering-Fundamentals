import sqlite3

def connect():
    return sqlite3.connect("students.db")

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")

def view_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent Records:")
    for student in students:
        print(student)

    conn.close()

def search_student():
    sid = int(input("Enter Student ID: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (sid,)
    )

    student = cursor.fetchone()

    if student:
        print(student)
    else:
        print("Student not found.")

    conn.close()

def update_student():
    sid = int(input("Enter Student ID: "))
    new_course = input("Enter New Course: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET course=? WHERE id=?",
        (new_course, sid)
    )

    conn.commit()
    conn.close()

    print("Student updated successfully!")

def delete_student():
    sid = int(input("Enter Student ID: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )

    conn.commit()
    conn.close()

    print("Student deleted successfully!")

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")