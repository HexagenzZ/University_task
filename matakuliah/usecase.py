from .model import Matakuliah
from .repo import MatakuliahRepo

class MatakuliahUsecase:
    def __init__(self):
        self.repo = MatakuliahRepo()

    def list(self):
        return self.repo.get_all()

    def detail(self, id):
        return self.repo.get_by_id(id)

    def create(self, nama_matakuliah, sks):
        mk = Matakuliah(None, nama_matakuliah, sks)
        self.repo.create(mk)

    def update(self, id, nama_matakuliah, sks):
        mk = Matakuliah(id, nama_matakuliah, sks)
        self.repo.update(id, mk)

    def delete(self, id):
        self.repo.delete(id)

