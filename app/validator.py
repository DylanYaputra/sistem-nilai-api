def validasi_nilai(nilai):
    return isinstance(nilai, (int, float)) and 0 <= nilai <= 100


def validasi_bobot(*bobot):
    return all(isinstance(b, (int, float)) for b in bobot) and sum(bobot) == 100
