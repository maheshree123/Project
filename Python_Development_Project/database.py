import sqlite3

DB_NAME = "volunteers.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS volunteers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT,
        phone TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()

def add_volunteer(name, age, city, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO volunteers(name, age, city, phone)
    VALUES (?, ?, ?, ?)
    """, (name, age, city, phone))

    conn.commit()
    conn.close()

def get_all_volunteers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM volunteers")
    data = cursor.fetchall()

    conn.close()
    return data

def search_volunteer(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM volunteers
    WHERE name LIKE ?
    """, ('%' + keyword + '%',))

    data = cursor.fetchall()

    conn.close()
    return data

def volunteer_exists(phone):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM volunteers WHERE phone=?",
        (phone,)
    )

    result = cursor.fetchone()

    conn.close()

    return result

def delete_volunteer(volunteer_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM volunteers WHERE id=?",
        (volunteer_id,)
    )

    conn.commit()
    conn.close()

def total_volunteers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM volunteers")

    total = cursor.fetchone()[0]

    conn.close()
    return total