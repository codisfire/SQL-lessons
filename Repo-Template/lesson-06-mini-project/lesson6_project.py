import sqlite3

connection = sqlite3.connect("school.db")
# Cursor executes SQL commands and reads query results
cursor = connection.cursor()

# Create the books table once, then reuse it on later runs
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

# Reset demp data so lesson output stays consistent/.
cursor.execute("DELETE FROM books")

# Add sample book records
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Holes", "Louis Sachar"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Wonder", "R. J. Palacio"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Hobbit", "J. R. R. Tolkien"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Life Story of Yuna Shin", "Yuna Shin"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("The Life Story of Arisa Komatsu", "Arisa Komatsu"))

#Query all books in alphabetical ordeer by title
cursor.execute("SELECT title, author FROM books ORDER BY title")

# fetchall() gives a list of (title, author) tuples to loop through
for title, author in cursor.fetchall():
    print(f"{title} by {author}")

# commit saves inserted rows to the database file
connection.commit()
connection.close()
