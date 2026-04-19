def hitung_nilai_akhir(tugas, uts, uas, kehadiran,
                       bobot_tugas, bobot_uts, bobot_uas, bobot_kehadiran):

    return (
        tugas * bobot_tugas / 100 +
        uts * bobot_uts / 100 +
        uas * bobot_uas / 100 +
        kehadiran * bobot_kehadiran / 100
    )


def konversi_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def predikat_akademik(grade):
    predikat = {
        "A": "Sangat Baik",
        "B": "Baik",
        "C": "Cukup",
        "D": "Kurang",
        "E": "Sangat Kurang"
    }
    return predikat.get(grade, "Tidak Diketahui")


def kategori_kinerja(nilai):
    if nilai >= 90:
        return "Excellent Student"
    elif nilai >= 80:
        return "High Performer"
    elif nilai >= 70:
        return "Average"
    else:
        return "Needs Improvement"


def status_kelulusan(nilai):
    return "LULUS" if nilai >= 65 else "TIDAK LULUS"
