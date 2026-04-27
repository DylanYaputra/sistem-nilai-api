import pytest
from app.api import app

# =========================
# Setup test client
# =========================

@pytest.fixture
def client():
    # Mengaktifkan mode testing Flask
    app.testing = True
    # Membuat client untuk simulasi request ke API
    return app.test_client()


# =========================
# API Endpoint tests
# =========================

def test_home(client):
    # Menguji endpoint root "/" apakah bisa diakses
    response = client.get("/")
    # Harus return status 200 (OK)
    assert response.status_code == 200


def test_hitung_nilai_success(client):
    # Menguji endpoint /hitung-nilai dengan input valid
    response = client.post("/hitung-nilai", json={
        "tugas": 80,
        "uts": 80,
        "uas": 80,
        "kehadiran": 80,
        "bobot_tugas": 25,
        "bobot_uts": 25,
        "bobot_uas": 25,
        "bobot_kehadiran": 25
    })

    # Harus berhasil (200 OK)
    assert response.status_code == 200

    # Response harus mengandung key "nilai_akhir"
    assert "nilai_akhir" in response.json


def test_invalid_nilai(client):
    # Menguji jika ada nilai tidak valid (>100)
    response = client.post("/hitung-nilai", json={
        "tugas": 200,  # invalid
        "uts": 80,
        "uas": 80,
        "kehadiran": 80,
        "bobot_tugas": 25,
        "bobot_uts": 25,
        "bobot_uas": 25,
        "bobot_kehadiran": 25
    })

    # Harus gagal (Bad Request)
    assert response.status_code == 400


def test_invalid_bobot(client):
    # Menguji jika total bobot tidak sama dengan 100
    response = client.post("/hitung-nilai", json={
        "tugas": 80,
        "uts": 80,
        "uas": 80,
        "kehadiran": 80,
        "bobot_tugas": 30,
        "bobot_uts": 30,
        "bobot_uas": 30,
        "bobot_kehadiran": 30
    })

    # Harus gagal karena validasi bobot tidak terpenuhi
    assert response.status_code == 400


def test_missing_data(client):
    # Menguji jika request tidak mengirim data (kosong)
    response = client.post("/hitung-nilai", json={})

    # Harus gagal karena data tidak lengkap
    assert response.status_code == 400
