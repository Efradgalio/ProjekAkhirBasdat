from django import forms


class Toko(forms.Form):
    nama_toko = forms.CharField(max_length=20)
    no_telepon = forms.IntegerField()
    alamat = forms.CharField(
        widget=forms.Textarea
    )

    deskripsi_singkat = forms.CharField(
        widget=forms.Textarea
    )


class Barang(forms.Form):
    nama_barang = forms.CharField(max_length=20)
    deskripsi_barang = forms.CharField(
        widget=forms.Textarea
    )
    harga = forms.FloatField()
    jumlah = forms.IntegerField()


class Login(forms.Form):
    nama_toko = forms.CharField(max_length=20)
    no_telepon = forms.IntegerField()
