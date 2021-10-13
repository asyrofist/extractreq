# Troubleshooting / FAQ Guide

Bagaimana jika menemukan masalah, seperti ini dikemudian hari, apabila saat menggunakan package ini. Maka muncul error seperti ini

## `No module not found`

portray raises this exception when it cant find a project in the current directory.
This means that there is no `pyproject.toml` or `setup.py` file in the directory you ran portray
AND that you haven't specified modules to include on the command line.

### Solution 1: instalasi terlebih dahulu requirements.txt
If you do have a `requirements.txt` sehingga cukup instalasi dengan cara menginstal semua modul yang dibutuhkan dalam package ini. Dengan cara 
```python
pip install -r requirements.txt
```

### Solution 2: Hubungi pihak admin
apabila dikemudian hari, anda menemukan masalah yang lebih spesifik. Alangkah lebih baiknya, anda cukup menghubungi `asyrofi.19051@mhs.its.ac.id` agar segera ditangani dan dikerjakan secara cepat.

### Solution 3: Gunakanlah demostrasi
Apabila, anda hanya mencoba aplikasi yang digunakan. Ada baiknya, sekarang anda tinggal mengklik tombol `live demo` dari keterangan deskripsi `README.md`. Sehingga agar dapat mempermudah anda.


## Akhir Kata dari Penulis

Baik itu saja, yang akan saya sampaikan. Semoga tidak ada kesalahan, atau error yang berarti dalam menggunakan package ini. Baik, saya ucapkan happy coding.. semoga bermanfaat
