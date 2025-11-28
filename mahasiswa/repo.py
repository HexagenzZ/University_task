# di file ini tuh bakal dipakai buat interact sama database, serti yang ada di bawah,
# banyak query DATABASE nya

# psycopg2 fungisnya buat apa ?
# ya buat komunikasi sama databasenya, dan juga buat koneksinya

# from database itu magging database yang udah di connect ini pakai file yang ada di 
# database

from database import get_db
import psycopg2.extras

class MahasiswaRepo:

    # ini tuh function buat nampilin semua data yang ada di databse dengan table mahasiswa,
    # seperty querynya yang SELECT * FROM MAHASISWA dan juga urutannya bakal berdasarakan 
    # dengan id

    # cur itu fungsinya kaya cursor, ibaratnya kalau get all ini berarti cursornya ada
    # di semua data yang ada di database
    def get_all(self):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM mahasiswa ORDER BY id;")
        data = cur.fetchall()
        cur.close(); conn.close()
        return data 

    # kalau yang ini funtion buat get single nya, liat query SQL nya kan ada 
    # WHERE id = kan, nah ntar id yang kepanggil bakal ditampilin
    # dan juga cursornya bakal ada di id itu doang, dibuktikan dengan fetchone
    def get_by_id(self, id):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM mahasiswa WHERE id=%s;", (id,))
        data = cur.fetchone()
        cur.close(); conn.close()
        return data

    # kalau yang ini buat POST, yang kaya di handler itu, buat ngirim data
    # querynya pakai INSERT, yang artinya itu masukin data ke database, any question ?
    def create(self, mhs):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO mahasiswa (nim, nama, jurusan) VALUES (%s, %s, %s)",
                    (mhs.nim, mhs.nama, mhs.jurusan))
        conn.commit()
        cur.close(); conn.close()
    
    # ini funtion buat update datanya yang ada di database,  bisa dipaka buat ganti nim,
    # nama, id dan juga jurusan (dalam case ini), query SQL nya pakai UPDATE yang dipakai
    # buat ngelakuin perubahan data

    def update(self, id, mhs):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE mahasiswa 
            SET nim=%s, nama=%s, jurusan=%s
            WHERE id=%s
        """, (mhs.nim, mhs.nama, mhs.jurusan, id))
        conn.commit()
        cur.close(); conn.close()

    # ini funtion buat ngelakuin delete datanya, set aja deletenya berdasarkan id yang bakal
    # mau didelete

    def delete(self, id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM mahasiswa WHERE id=%s", (id,))
        conn.commit()
        cur.close(); conn.close()

