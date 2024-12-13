import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Borrowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO Authors (name) VALUES ('Лев Толстой')")
cursor.execute("INSERT INTO Authors (name) VALUES ('Федор Достоевский')")

cursor.execute("INSERT INTO Books (title, author_id) VALUES ('Война и мир', 1)")
cursor.execute("INSERT INTO Books (title, author_id) VALUES ('Преступление и наказание', 2)")

cursor.execute("INSERT INTO Borrowers (name) VALUES ('Иван Иванов')")
cursor.execute("INSERT INTO Borrowers (name) VALUES ('Мария Петрова')")

conn.commit()
conn.close()