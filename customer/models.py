from django.db import models
from django .contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class TokoModel(models.Model):
    nama_toko = models.CharField(max_length=20)
    no_telepon = models.IntegerField()
    alamat = models.TextField()
    deskripsi_singkat = models.TextField()
    nama_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_toko)

    def get_absolute_url(self):
        return reverse('customer:toko-detail', kwargs={'pk': self.pk})


class BarangModel(models.Model):
    nama_barang = models.CharField(max_length=200)
    deskripsi_barang = models.TextField()
    harga = models.CharField(max_length=10)
    jumlah_tersedia = models.IntegerField()
    gambar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    nama_tokos = models.ForeignKey(TokoModel, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nama_barang) + ": Rp." + self.harga

    def get_absolute_url(self):
        return reverse('barang-detail', kwargs={'pk': self.pk})


class OrderModel(models.Model):
    tanggal = models.CharField(max_length=20)
    toko = models.ForeignKey(TokoModel, default=None, on_delete=models.CASCADE)
    barang = models.ForeignKey(BarangModel, default=None, on_delete=models.CASCADE)
