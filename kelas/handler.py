from flask import Blueprint, request, jsonify
from .usecase import KelasUsecase

kelas_bp = Blueprint("kelas", __name__)
usecase = KelasUsecase()

@kelas_bp.get("/")
def list_kelas():
    return jsonify([dict(row) for row in usecase.list()])

@kelas_bp.get("/<int:id>")
def detail_kelas(id):
    return jsonify(dict(usecase.detail(id)))

@kelas_bp.post("/")
def create_kelas():
    data = request.json
    usecase.create(
        data["mahasiswa_id"],
        data["matakuliah_id"],
        data["semester"]
    )
    return jsonify({"message": "Kelas created"})

@kelas_bp.put("/<int:id>")
def update_kelas(id):
    data = request.json
    usecase.update(
        id,
        data["mahasiswa_id"],
        data["matakuliah_id"],
        data["semester"]
    )
    return jsonify({"message": "Kelas updated"})

@kelas_bp.delete("/<int:id>")
def delete_kelas(id):
    usecase.delete(id)
    return jsonify({"message": "Kelas deleted"})

