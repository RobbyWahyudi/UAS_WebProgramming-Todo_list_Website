from django.db import models
from django.contrib.auth.models import User


class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class Task(models.Model):
    PILIHAN_STATUS = [
        ("belum_selesai", "Belum Selesai"),
        ("Selesai", "selesai"),
    ]

    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tanggal_jatuh_tempo = models.DateField()
    status = models.CharField(
        max_length=20, choices=PILIHAN_STATUS, default="Belum Selesai"
    )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
