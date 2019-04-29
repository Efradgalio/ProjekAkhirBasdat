from django.db import models

# Create your models here.


class LoginModel(models.Model):
    nama = models.CharField(max_length=20)
    no_hp = models.IntegerField()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)


class TokoModel(models.Model):
    nama_toko = models.CharField(max_length=20)
    no_telepon = models.IntegerField()
    alamat = models.TextField()
    deskripsi_singkat = models.TextField()
    nama_user = models.ForeignKey(LoginModel, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)
