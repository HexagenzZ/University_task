from database import get_db
import psycopg2.extras

class MatakuliahRepo:

    def get_all(self):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM matakuliah ORDER BY id;")
        data = cur.fetchall()
        cur.close(); conn.close()
        return data

    def get_by_id(self, id):
        conn = get_db()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM matakuliah WHERE id=%s;", (id,))
        data = cur.fetchone()
        cur.close(); conn.close()
        return data

    def create(self, mk):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO matakuliah (nama_matakuliah, sks) VALUES (%s, %s)",
                    (mk.nama_matakuliah, mk.sks))
        conn.commit()
        cur.close(); conn.close()

    def update(self, id, mk):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE matakuliah 
            SET nama_matakuliah=%s, sks=%s
            WHERE id=%s
        """, (mk.nama_matakuliah, mk.sks, id))
        conn.commit()
        cur.close(); conn.close()

    def delete(self, id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM matakuliah WHERE id=%s", (id,))
        conn.commit()
        cur.close(); conn.close()

