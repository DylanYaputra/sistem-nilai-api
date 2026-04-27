
# Validator tests

def test_validasi_nilai_valid():
    # Menguji bahwa nilai dalam rentang valid (0–100) dianggap benar
    assert validasi_nilai(50) is True

def test_validasi_nilai_invalid():
    # Menguji bahwa nilai di luar rentang valid (lebih dari 100) dianggap salah
    assert validasi_nilai(150) is False

def test_validasi_bobot_valid():
    # Menguji bahwa total bobot yang tepat (jumlah = 100) dianggap valid
    assert validasi_bobot(25, 25, 25, 25) is True

def test_validasi_bobot_invalid():
    # Menguji bahwa total bobot yang tidak sama dengan 100 dianggap tidak valid
    assert validasi_bobot(30, 30, 30, 30) is False


# Service tests

def test_hitung_nilai():
    # Menguji perhitungan nilai akhir dengan nilai dan bobot seimbang
    # Semua nilai 80 dan bobot sama → hasil akhir harus 80
    assert hitung_nilai_akhir(80, 80, 80, 80, 25, 25, 25, 25) == 80

def test_grade_A():
    # Menguji konversi nilai ke grade A (nilai tinggi)
    assert konversi_grade(90) == "A"

def test_grade_C():
    # Menguji konversi nilai ke grade C (nilai menengah)
    assert konversi_grade(65) == "C"

def test_predikat():
    # Menguji mapping grade ke predikat akademik
    # Grade A → "Sangat Baik"
    assert predikat_akademik("A") == "Sangat Baik"

def test_kategori():
    # Menguji kategori kinerja untuk nilai tinggi
    # Nilai 85 → "High Performer"
    assert kategori_kinerja(85) == "High Performer"

def test_status_lulus():
    # Menguji status kelulusan untuk nilai di atas batas lulus
    # Nilai 70 → "LULUS"
    assert status_kelulusan(70) == "LULUS"

def test_status_tidak_lulus():
    # Menguji status kelulusan untuk nilai di bawah batas lulus
    # Nilai 50 → "TIDAK LULUS"
    assert status_kelulusan(50) == "TIDAK LULUS"

# Boundary & tambahan tests

def test_boundary_0():
    # Menguji batas bawah nilai (0 masih valid)
    assert validasi_nilai(0) is True

def test_boundary_100():
    # Menguji batas atas nilai (100 masih valid)
    assert validasi_nilai(100) is True

def test_grade_E():
    # Menguji konversi nilai sangat rendah ke grade E
    assert konversi_grade(30) == "E"

def test_kategori_low():
    # Menguji kategori kinerja untuk nilai rendah
    # Nilai 60 → "Needs Improvement"
    assert kategori_kinerja(60) == "Needs Improvement"  