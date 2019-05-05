from django.shortcuts import render
from customer.models import BarangModel
from django.views.generic import ListView, DetailView, CreateView
from customer.forms import Barang


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


class BarangCreateView(CreateView):
    model = BarangModel
    fields = ['nama_barang', 'deskripsi_barang', 'harga', 'jumlah_tersedia', 'gambar', 'nama_tokos']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.nama_tokos.nama_user = self.request.user
        return super().form_valid(form)
