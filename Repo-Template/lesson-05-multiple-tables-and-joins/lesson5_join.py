import sqlite3

connection = sqlite3.connect("school.db")
#Cursor is the command runner for every SQL statement in this script
cursor = connection.cursor()

# Build the first tale
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID integer PRIMARY KEY, 
    name TEXT NOT NULL, 
    year_group INTEGER
)
""")

#Build the second table, which stores the related student_id value
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_id INTEGER
)
""")

# Remove old data so each run starts cleanly
cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM courses")

cursor.execute(
    "INSERT INTO students (name, year_group) VALUES (?, ?)",
    ("Ava", 10)
)

