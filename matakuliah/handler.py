from flask import Blueprint, request, jsonify
from .usecase import MatakuliahUsecase

mk_bp = Blueprint("matakuliah", __name__)
usecase = MatakuliahUsecase()

@mk_bp.get("/")
def list_mk():
    return jsonify([dict(row) for row in usecase.list()])

@mk_bp.get("/<int:id>")
def detail_mk(id):
    return jsonify(dict(usecase.detail(id)))

@mk_bp.post("/")
def create_mk():
    data = request.json
    usecase.create(data["nama_matakuliah"], data["sks"])
    return jsonify({"message": "Matakuliah created"})

@mk_bp.put("/<int:id>")
def update_mk(id):
    data = request.json
    usecase.update(id, data["nama_matakuliah"], data["sks"])
    return jsonify({"message": "Matakuliah updated"})

@mk_bp.delete("/<int:id>")
def delete_mk(id):
    usecase.delete(id)
    return jsonify({"message": "Matakuliah deleted"})

