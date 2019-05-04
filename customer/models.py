from django.db import models
from django .contrib.auth.models import User
# Create your models here.


class TokoModel(models.Model):
    nama_toko = models.CharField(max_length=20)
    no_telepon = models.IntegerField()
    alamat = models.TextField()
    deskripsi_singkat = models.TextField()
    nama_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_toko)


class BarangModel(models.Model):
    nama_barang = models.CharField(max_length=200)
    deskripsi_barang = models.TextField()
    harga = models.CharField(max_length=10)
    jumlah_tersedia = models.IntegerField()
    gambar = models.ImageField(upload_to='profile_pics/')
    nama_tokos = models.ForeignKey(TokoModel, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nama_barang) + ": Rp." + self.harga
