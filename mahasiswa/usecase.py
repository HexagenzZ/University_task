# kalau file usecase ini iu buat ngejembatani antara handler dengan repo
# gambarannya kaya handler -> usecase -> repo
# handler kan fungsinya buat endpoitnnya, sedangkan repo itu buat interact sama db 
# nah usecase ini ada di tengah" nya, alasannya ? supaya semuanya punya tugas masing"
# handler itu kan buant merima request dari user
# usecase itu sebagai pemikirnya, misal nih mau POST maka di yang ngurus nim nya dah unik blm
# kalau repo ya sama database

from .model import Mahasiswa
from .repo import MahasiswaRepo

class MahasiswaUsecase:
    # function di bawah ini itu kaya kita ngomong ke sistem kaya, pakai table yang mahsiswa 
    # aja ya
    def __init__(self):
        self.repo = MahasiswaRepo()

    def list(self):
        return self.repo.get_all()

    def detail(self, id):
        return self.repo.get_by_id(id)

    def create(self, nim, nama, jurusan):
        mhs = Mahasiswa(None, nim, nama, jurusan)
        self.repo.create(mhs)

    def update(self, id, nim, nama, jurusan):
        mhs = Mahasiswa(id, nim, nama, jurusan)
        self.repo.update(id, mhs)

    def delete(self, id):
        self.repo.delete(id)

# di dalam file usecase ini kita bisa nge set aturan yang mau kita pakai, misal nya di 
# get_all nya itu kita set dengan tampilin datanya 50 aja, atau mahasiswa ini aja yang 
# ditampilin, jadinya handler hanya perlu request dari user aja, sedangkan usecase nya 
# buat ngasih aturan yang bakal dipakai di handler.

# dkode id atas itu belum aktif sepenuhnya
