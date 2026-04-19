# Sistem Nilai Mahasiswa API

## Deskripsi

Aplikasi REST API sederhana untuk menghitung nilai akhir mahasiswa, menentukan grade, predikat, dan status kelulusan.

## Cara Menjalankan

pip install -r requirements.txt
python -m flask --app app.api run

## Cara Testing

pytest --cov=app

## Testing Strategy

- Unit Test: Menguji fungsi logika bisnis
- Integration Test: Menguji endpoint API

## CI

Menggunakan GitHub Actions untuk:

- install dependency
- menjalankan test
- generate coverage
