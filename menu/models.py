from django.db import models


class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama


class Task(models.Model):
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tanggal_jatuh_tempo = models.DateField()
    status = models.CharField(max_length=20)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
