import sqlite3

conn = sqlite3.connect('prepaid_cards.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS PrepaidCard (
        CardNo VARCHAR(10) PRIMARY KEY,
        Balance DOUBLE,
        StudentID VARCHAR(10),
        FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
    )
''')

conn.commit()
conn.close()

print("PrepaidCard table created successfully.")
