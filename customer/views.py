from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Toko, Barang, Login
from .models import TokoModel
# Create your views here.


def index(request):

    context = {
        'page_title': 'Customer',
    }
    print(request.user)
    return render(request, 'customer/index.html', context)


def create(request):

    toko = Toko()

    if request.method == 'POST':
        TokoModel.objects.create(
            nama_toko=request.POST['nama_toko'],
            no_telepon=request.POST['no_telepon'],
            alamat=request.POST['alamat'],
            deskripsi_singkat=request.POST['deskripsi_singkat'],
        )
        return HttpResponseRedirect("/customer/list/")
    context = {
        'page_title': 'AYO DAFTAR TOKO ANDA',
        'toko': toko,
    }
    return render(request, 'customer/create.html', context)


def list(request):
    toko_all = TokoModel.objects.all()

    context = {
        'page_title': 'List Toko',
        'Toko': toko_all,
    }
    return render(request, 'customer/list.html', context)


def login(request):
    login = Login()
    context = {
        'page_title': 'Login Home',
        'login': login,

    }
    return render(request, 'customer/login.html', context)
