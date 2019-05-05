from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Toko, Barang, Login
from .models import TokoModel, BarangModel, OrderModel
# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'page_title': 'Customer',
    }

    return render(request, 'customer/index.html', context)


def list(request):
    toko_all = TokoModel.objects.all()

    context = {
        'page_title': 'List Toko',
        'Toko': toko_all,
    }
    return render(request, 'customer/list.html', context)


def login(request):
    context = {
        'page_title': 'Login Home',

    }
    if request.method == 'POST':
        # print(request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            return redirect("customer/login/")
    return render(request, 'customer/login.html', context)


def logout(request):
    context = {
        'page_title': 'logout'
    }
    if request.method == 'POST':
        if request.POST['logout'] == 'Kirim Kueri':
            auth_logout(request)
        return redirect("index")
    return render(request, 'customer/logout.html', context)


class TokoListView(ListView):
    model = TokoModel
    template_name = 'customer/list.html'  # <app>/<model>_<view type>.html
    context_object_name = 'Toko'
    # ordering = ['-date_posted'] --> Ordering New To Latest


class TokoDetailView(DetailView):
    model = TokoModel


class TokoCreateView(CreateView):
    model = TokoModel
    fields = ['nama_toko', 'no_telepon', 'alamat', 'deskripsi_singkat']

    def form_valid(self, form):
        form.instance.nama_user = self.request.user
        return super().form_valid(form)
