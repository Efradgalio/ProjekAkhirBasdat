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
