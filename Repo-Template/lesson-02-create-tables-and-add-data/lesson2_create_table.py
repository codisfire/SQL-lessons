import sqlite3

# Connect Python to the SQLite database file.
connection = sqlite3.connect("school.db")
# A cursor is the object that send SQL commands to the databse.
cursor = connection.cursor()

# Execute SQL to create the students table if it does not exist yet.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL, 
    year_group INTEGER,
    favorite_subject TEXT
)
""")

# Clear old rowqs so this lesson script gives predictable output each run.
cursor.execute("DELETE FROM students")

# Insert rows using placeholders (?) to safely pass Python values.
cursor.execute("INSERT INTO students (name, year_group, favorite_subject) VALUES (?, ?, ?)", ("Ava", 10, "PDPHE"))
cursor.execute("INSERT INTO students (name, year_group, favorite_subject) VALUES (?, ?, ?)", ("Leo", 10, "Math"))
cursor.execute("INSERT INTO students (name, year_group, favorite_subject) VALUES (?, ?, ?)", ("John", 12, "History"))
# commit saves all changes made by INSERT/DELETE/CREATE statements
connection.commit()
# Always close the connection when finished.
connection.close()