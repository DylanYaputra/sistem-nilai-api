import pytest
from app.service import *
from app.validator import *

# Validator tests
def test_validasi_nilai_valid():
    assert validasi_nilai(50) is True

def test_validasi_nilai_invalid():
    assert validasi_nilai(150) is False

def test_validasi_bobot_valid():
    assert validasi_bobot(25, 25, 25, 25) is True

def test_validasi_bobot_invalid():
    assert validasi_bobot(30, 30, 30, 30) is False


# Service tests
def test_hitung_nilai():
    assert hitung_nilai_akhir(80, 80, 80, 80, 25, 25, 25, 25) == 80

def test_grade_A():
    assert konversi_grade(90) == "A"

def test_grade_C():
    assert konversi_grade(65) == "C"

def test_predikat():
    assert predikat_akademik("A") == "Sangat Baik"

def test_kategori():
    assert kategori_kinerja(85) == "High Performer"

def test_status_lulus():
    assert status_kelulusan(70) == "LULUS"

def test_status_tidak_lulus():
    assert status_kelulusan(50) == "TIDAK LULUS"

# tambahan biar >= 15 test
def test_boundary_0():
    assert validasi_nilai(0) is True

def test_boundary_100():
    assert validasi_nilai(100) is True

def test_grade_E():
    assert konversi_grade(30) == "E"

def test_kategori_low():
    assert kategori_kinerja(60) == "Needs Improvement"
