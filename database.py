from config import DATABASE
import sqlite3

# membuat database jadwal pelajaran sekolah
day = [ (_,) for _ in (['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]
mapel_normatif = [ (_,) for _ in (['Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Sejarah', 'Seni Rupa', 'Pendidikan Agama Islam', 'PJOK', 'Bahasa Jawa', 'PPKN', 'Bahasa Inggris'])]
mapel_produktif = [ (_,) for _ in (['IPAS', 'Dasar-dasar Program Keahlian PPLG', 'Informatika', 'Koding dan Kecerdasan Artifisial'])]

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS Jadwal_Normatif
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             hari TEXT NOT NULL,
                             mata_pelajaran TEXT NOT NULL,
                             waktu TEXT NOT NULL);''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Jadwal_Produktif
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             hari TEXT NOT NULL,
                             mata_pelajaran TEXT NOT NULL,
                             waktu TEXT NOT NULL);''')
            conn.commit()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cursor = conn.execute(sql, data)
            cursor.execute(sql, data)
            return cursor.fetchall()
    
    def insert_JadwalNormatif(self, data):
        sql = 'INSERT OR IGNORE INTO Jadwal_Normatif (hari, mata_pelajaran, waktu) values(?, ?, ?)'
        data = [
            ('Senin', 'Matematika', '07:30 - 10:00'),
            ('Senin', 'Sejarah', '10:00 - 11:30'),
            ('Senin', 'Pendidikan Agama Islam', '12:00 - 13:30'),
            ('Senin', 'Bahasa Indonesia', '13:30 - 15:00'),
            ('Selasa', 'Sejarah', '06:45 - 08:15'),
            ('Selasa', 'Seni Rupa', '08:15 - 11:30'),
            ('Selasa', 'Bahasa Indonesia', '12:00 - 13:30'),
            ('Selasa', 'PJOK', '13:30 - 15:00'),
            ('Rabu', 'Bahasa Jawa', '06:45 - 07:30'),
            ('Rabu', 'Matematika', '07:30 - 10:00'),
            ('Rabu', 'PPKN', '10:00 - 11:30'),
            ('Rabu', 'Pendidikan Agama Islam', '12:00 - 13:30'),
            ('Rabu', 'Bahasa Inggris', '13:30 - 15:00'),
            ('Kamis', 'PJOK', '06:45 - 10:00'),
            ('Kamis', 'Pendidikan Agama Islam', '10:00 - 11:30'),
            ('Kamis', 'Bahasa Inggris', '12:00 - 13:30'),
            ('Kamis', 'PPKN', '13:30 - 15:00'),
            ('Jumat', 'Bahasa Inggris', '07:45 - 09:15'),
            ('Jumat', 'Bahasa Indonesia', '09:30 - 11:00'),
        ]
        self.__executemany(sql, data)

    def insert_JadwalProduktif(self, data):
        sql = 'INSERT OR IGNORE INTO Jadwal_Produktif (hari, mata_pelajaran, waktu) values(?, ?, ?)'
        data = [
            ('Senin', 'IPAS', '07:30 - 10:00'),
            ('Senin', 'Dasar-dasar Program Keahlian PPLG', '10:00 - 12:45'),
            ('Senin', 'Informatika', '12:45 - 15:00'),
            ('Selasa', 'Dasar-dasar Program Keahlian PPLG', '06:45 - 09:00'),
            ('Selasa', 'Informatika', '09:15 - 11:30'),
            ('Selasa', 'IPAS', '12:00 - 15:00'),
            ('Rabu', 'Dasar-dasar Program Keahlian PPLG', '06:45 - 09:00'),
            ('Rabu', 'IPAS', '09:15 - 11:30'),
            ('Rabu', 'Dasar-dasar Program Keahlian PPLG', '12:00 - 15:00'),
            ('Kamis', 'Dasar-dasar Program Keahlian PPLG', '06:45 - 10:00'),
            ('Kamis', 'Dasar-dasar Program Keahlian PPLG', '10:00 - 15:00'),
            ('Jumat', 'Koding dan Kecerdasan Artifisial', '07:45 - 09:15'),
            ('Jumat', 'Koding dan Kecerdasan Artifisial', '09:30 - 11:00'),
        ]
        self.__executemany(sql, data)

    def get_JadwalNormatif(self, hari):
        sql = 'SELECT * FROM "Jadwal_Normatif" WHERE hari = ?'
        data = (hari,)
        return self.__select_data(sql, data)
    
    def get_JadwalProduktif(self, hari):
        sql = 'SELECT * FROM "Jadwal_Produktif" WHERE hari = ?'
        data = (hari,)
        return self.__select_data(sql, data)
    
    def populate_initial_data(self):
        self.insert_JadwalNormatif(mapel_normatif)
        self.insert_JadwalProduktif(mapel_produktif)
    
if __name__ == "__main__":
    db_manager = DB_Manager(DATABASE)
    db_manager.create_tables()
    db_manager.populate_initial_data()