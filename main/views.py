from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import ProductForm
from main.models import Product, Contact, Order, Version


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductListView(GetContextMixin, ListView):
    model = Product


class ProductDetailView(GetContextMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')


class ContactListView(ListView):
    model = Contact


class OrderCreateView(CreateView):
    model = Order  # Модель
    fields = ('name', 'phone', 'message', 'created_at')  # Поля для заполнения при создании
    success_url = reverse_lazy('main:product_list')  # Адрес для перенаправления после успешного создания

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response



