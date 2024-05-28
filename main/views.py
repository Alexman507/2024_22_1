from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from main.models import Product, Contact, Order


# Create your views here.

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


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
