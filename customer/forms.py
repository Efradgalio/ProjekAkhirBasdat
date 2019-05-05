from django import forms
from .models import TokoModel, BarangModel


class Toko(forms.ModelForm):
    # nama_toko = forms.CharField(max_length=20)
    # no_telepon = forms.IntegerField()
    # alamat = forms.CharField(
    #     widget=forms.Textarea
    # )

    # deskripsi_singkat = forms.CharField(
    #     widget=forms.Textarea
    # )

    class Meta:
        model = TokoModel
        fields = ['nama_toko', 'no_telepon', 'alamat', 'deskripsi_singkat']
        exclude = ('key_field',)


class Barang(forms.ModelForm):
    # nama_barang = forms.CharField(max_length=20)
    # deskripsi_barang = forms.CharField(
    #     widget=forms.Textarea
    # )
    # harga = forms.FloatField()
    # jumlah = forms.IntegerField()
    # gambar = forms.ImageField()
    class Meta:
        model = BarangModel
        fields = ['nama_barang', 'deskripsi_barang', 'harga', 'jumlah_tersedia', 'gambar']
        exclude = ('key_field',)


class Login(forms.Form):
    nama_toko = forms.CharField(max_length=20)
    no_telepon = forms.IntegerField()
