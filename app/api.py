from flask import Flask, request, jsonify
from app.service import (
    hitung_nilai_akhir,
    konversi_grade,
    predikat_akademik,
    kategori_kinerja,
    status_kelulusan
)
from app.validator import validasi_nilai, validasi_bobot

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "API Sistem Nilai Mahasiswa"})


@app.route("/hitung-nilai", methods=["POST"])
def hitung():
    data = request.get_json()

    try:
        tugas = data["tugas"]
        uts = data["uts"]
        uas = data["uas"]
        kehadiran = data["kehadiran"]

        bobot_tugas = data["bobot_tugas"]
        bobot_uts = data["bobot_uts"]
        bobot_uas = data["bobot_uas"]
        bobot_kehadiran = data["bobot_kehadiran"]
    except KeyError:
        return jsonify({"error": "Data tidak lengkap"}), 400

    # Validasi nilai
    if not all(validasi_nilai(n) for n in [tugas, uts, uas, kehadiran]):
        return jsonify({"error": "Nilai harus 0-100"}), 400

    # Validasi bobot
    if not validasi_bobot(bobot_tugas, bobot_uts, bobot_uas, bobot_kehadiran):
        return jsonify({"error": "Total bobot harus 100"}), 400

    nilai_akhir = hitung_nilai_akhir(
        tugas, uts, uas, kehadiran,
        bobot_tugas, bobot_uts, bobot_uas, bobot_kehadiran
    )

    grade = konversi_grade(nilai_akhir)

    return jsonify({
        "nilai_akhir": round(nilai_akhir, 2),
        "grade": grade,
        "predikat": predikat_akademik(grade),
        "kategori": kategori_kinerja(nilai_akhir),
        "status": status_kelulusan(nilai_akhir)
    })
