from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,  UpdateView, DeleteView, TemplateView, RedirectView, FormView
from .models import Product
from django.urls import reverse_lazy



def main(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login-register.html')


def register(request):
    return render(request, 'login-register.html')

class Product(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
    paginate_by = 10


class Product(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class Product(CreateView):
    model = Product
    template_name = 'product.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class Product(UpdateView):
    model = Product
    template_name = 'product.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class Product(DeleteView):
    model = Product
    template_name = 'base.html'
    success_url = reverse_lazy('product_list')



class YourTemplateView(TemplateView):
    template_name = 'base.html'




