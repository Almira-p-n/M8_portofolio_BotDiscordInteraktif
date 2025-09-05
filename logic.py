from config import DATABASE
import sqlite3

# membuat database jadwal pelajaran sekolah
day = [ (_,) for _ in (['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]
subject = []

def create_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS schedule
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  day TEXT NOT NULL,
                  subject TEXT NOT NULL,
                  time TEXT NOT NULL)''')
    conn.commit()
    conn.close()