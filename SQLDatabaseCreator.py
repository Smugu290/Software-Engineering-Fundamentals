import sqlite3

# Create/connect to database
conn = sqlite3.connect("students.db")

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database created successfully!")