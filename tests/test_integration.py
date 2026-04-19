import pytest
from app.api import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_hitung_nilai_success(client):
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
    assert response.status_code == 200
    assert "nilai_akhir" in response.json


def test_invalid_nilai(client):
    response = client.post("/hitung-nilai", json={
        "tugas": 200,
        "uts": 80,
        "uas": 80,
        "kehadiran": 80,
        "bobot_tugas": 25,
        "bobot_uts": 25,
        "bobot_uas": 25,
        "bobot_kehadiran": 25
    })
    assert response.status_code == 400


def test_invalid_bobot(client):
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
    assert response.status_code == 400


def test_missing_data(client):
    response = client.post("/hitung-nilai", json={})
    assert response.status_code == 400
