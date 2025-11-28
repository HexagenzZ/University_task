from .model import Kelas
from .repo import KelasRepo

class KelasUsecase:
    def __init__(self):
        self.repo = KelasRepo()

    def list(self):
        return self.repo.get_all()

    def detail(self, id):
        return self.repo.get_by_id(id)

    def create(self, mahasiswa_id, matakuliah_id, semester):
        ke = Kelas(None, mahasiswa_id, matakuliah_id, semester)
        self.repo.create(ke)

    def update(self, id, mahasiswa_id, matakuliah_id, semester):
        ke = Kelas(id, mahasiswa_id, matakuliah_id, semester)
        self.repo.update(id, ke)

    def delete(self, id):
        self.repo.delete(id)

