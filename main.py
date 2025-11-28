from flask import Flask
from mahasiswa.handler import mhs_bp
from matakuliah.handler import mk_bp
from kelas.handler import kelas_bp
from database import get_db

# ini inisialisai buat yang kita pakai itu flask
app = Flask(__name__)

# ini kaya yang ada di handler yaitu buat set url nya.
app.register_blueprint(mhs_bp, url_prefix="/mahasiswa")
app.register_blueprint(mk_bp, url_prefix="/matakuliah")
app.register_blueprint(kelas_bp, url_prefix="/kelas")

# ini buat nge test connection ke databasenya udah jalan dan connect atau belum
# endpointnya ada di /test-db, kalau dah connect succes bakal ada response
# Dtabase Connected
@app.get("/test-db")
def test_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        return {"status": "OK", "message": "Database Connected!"}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)

