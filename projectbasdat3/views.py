from django.shortcuts import render
from customer.models import BarangModel
from django.views.generic import ListView, DetailView


def index(request):
    barang_all = BarangModel.objects.all()
    context = {
        'page_title': 'Home',
        'Barang': barang_all,
    }

    return render(request, 'index.html', context)


class BarangListView(ListView):
    model = BarangModel
    template_name = 'index.html'
    context_object_name = 'Barang'


class BarangDetailView(DetailView):
    model = BarangModel
