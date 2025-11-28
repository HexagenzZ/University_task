# Import library yang bakal diperluin dulu disini

# Blueprint itu dipakai buat modularisasi atau mecahin kode di project yang
# - dipakai jadi bagian kecil", contohnya itu ada di @mhsbp, nah misal kalau 
# mau pakai yang get bakal yang get aja kepanggil
# dan juga di kode ini bakal dipakai buat nge set url nya
# misal di main.py itu kan ada set url prefix /mahasiswa, nanti burl nya bagian 
# yang dipanggil bakal jadi /mahasiswa juga

# Request ini bakal dipakai buat ya request wkwk
# maksudnya ngambil data yang dikirim dari client ke server
# misal nih bagian request.json, nah itu set data yag dikirim jadi json

# jsonify, ini tuh bantu buat ngehindarin kita sebagai dev buat data JSON 
#  nya secara manual

from flask import Blueprint, request, jsonify
from .usecase import MahasiswaUsecase

# kode di bawah ini seperti yang idjelasin di awawl, yaitu url nya bakal ke set di /mahasiswa

mhs_bp = Blueprint("mahasiswa", __name__, url_prefix="/mahasiswa")
usecase = MahasiswaUsecase()

# di kode di bawah ini ke set endpoint buat GET nya yang artinya bakal ngambil data 
# sluruh mahasiswa yang dah ke POST, simplenya kaya ambil emua data yang dah kekirim 
# di database.

# terus di dalam endpoint yang di set ini ada functionnya (list_mhs)
# functionnya bakal ngasih data dalam bentuk json
# cara kerjanya yaitu ngambil semua data yang ada di database di table mahasiswa, 
# terus datanya diubah ke bentuk json pakai jsonify 

@mhs_bp.get("/")
def list_mhs():
    return jsonify([dict(row) for row in usecase.list()])


# yang ini cara kerjanya sama aja, tapi yang ditampilin hanya satu mahasiswa yang punya
# id yang dah di set, misal id di databasenya itu 1 maka jika /mahasiswa/1 maka 
# data mahasiswa itu yang ditampilin

@mhs_bp.get("/<int:id>")
def detail_mhs(id):
    return jsonify(dict(usecase.detail(id)))

# kalau yang ini itu POST, gunanya buat ngirim data ke database, fromat data yang dikirim
# itu pakai json dan juga nakal nampilin response "Mahasiswa created" kalau success
# misal, kita kirim datanya, dalam case ini kirim dengan nim, nama dan jurusan, nah ntar
# bakal ada di database. id nya ? dah otomatis ke set

@mhs_bp.post("/")
def create_mhs():
    data = request.json
    usecase.create(data["nim"], data["nama"], data["jurusan"])
    return jsonify({"message": "Mahasiswa created"})

# ini tuh buat ngupdate data yang ada di db,
# langsung ke case nya aja, misal ada mahasiswa dengan  ID 5, nama: Anto
# terus kita mau ngubah namanya ke Andi, tinggal set id nya berapa terus lakuin update
# maka mahasiswa dengan id 5 itu jadi Andi bukan Anto lagi.

@mhs_bp.put("/<int:id>")
def update_mhs(id):
    data = request.json
    usecase.update(id, data["nim"], data["nama"], data["jurusan"])
    return jsonify({"message": "Mahasiswa updated"})


# ini buat nge hapus daa nya mahasiswanya, cara kerjanya ?
# sama kaya yang detail_mahasiswa, set /mahasiswa/id, id pakai yang mau dihapus
# terus set actionnya jadi delete, dan data nya bakal kehapus

@mhs_bp.delete("/<int:id>")
def delete_mhs(id):
    usecase.delete(id)
    return jsonify({"message": "Mahasiswa deleted"})

