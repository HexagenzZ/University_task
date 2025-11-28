from database import get_db
import psycopg2.extras

class KelasRepo:

    def get_all(self):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("""
            SELECT 
                kelas.id,
                kelas.semester,
                mahasiswa.nama AS mahasiswa,
                matakuliah.nama_matakuliah AS matakuliah
            FROM kelas
            JOIN mahasiswa ON kelas.mahasiswa_id = mahasiswa.id
            JOIN matakuliah ON kelas.matakuliah_id = matakuliah.id
            ORDER BY kelas.id;
        """)

        rows = cur.fetchall()
        cur.close(); conn.close()
        return rows

    def get_by_id(self, id):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * FROM kelas WHERE id=%s", (id,))
        row = cur.fetchone()

        cur.close(); conn.close()
        return row

    def create(self, kelas):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO kelas (mahasiswa_id, matakuliah_id, semester)
            VALUES (%s, %s, %s)
        """, (kelas.mahasiswa_id, kelas.matakuliah_id, kelas.semester))

        conn.commit()
        cur.close(); conn.close()

    def update(self, id, kelas):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            UPDATE kelas 
            SET mahasiswa_id=%s, matakuliah_id=%s, semester=%s
            WHERE id=%s
        """, (kelas.mahasiswa_id, kelas.matakuliah_id, kelas.semester, id))

        conn.commit()
        cur.close(); conn.close()

    def delete(self, id):
        conn = get_db()
        cur = conn.cursor()

        cur.execute("DELETE FROM kelas WHERE id=%s", (id,))
        conn.commit()

        cur.close(); conn.close()

