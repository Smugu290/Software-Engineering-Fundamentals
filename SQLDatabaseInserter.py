import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Pratz", 20)
)

conn.commit()
conn.close()

print("Data inserted!")
