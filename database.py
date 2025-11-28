import psycopg2
import psycopg2.extras

def get_db():
    return psycopg2.connect(
        host="localhost",
        database="university",
        user="postgres",
        password=""
    )

# ini buat connect ke database nya, di sini dah di set nama databasenya apa, portnya apa dll
# psycopg2.extras itu buat ngasih fitur  tambahan kaya cursor yang ada di repo 
