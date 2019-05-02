from django.shortcuts import render
from customer.models import BarangModel


def index(request):
    barang_all = BarangModel.objects.all()
    context = {
        'page_title': 'Home',
        'Barang': barang_all,
    }

    return render(request, 'index.html', context)
