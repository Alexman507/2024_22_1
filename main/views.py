from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.form import ProductForm
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


class ProductUpdateWithSubjectsView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('myapp:list')


def get_context_data(self, **kwargs):
    context_data = super().get_context_data(**kwargs)
    FormSet = inlineformset_factory(self.model, Subject, form=SubjectForm, extra=1)
    if self.request.method == 'POST':
        formset = FormSet(self.request.POST, instance=self.object)
    else:
        formset = FormSet(instance=self.object)
    context_data['formset'] = formset
    return context_data


def form_valid(self, form):
    context_data = self.get_context_data()
    formset = context_data['formset']
    with transaction.atomic():
        if form.is_valid():
            self.object = form.save()  # Student
            if formset.is_valid():
                formset.instance = self.object
                formset.save()  # Subject

    return super().form_valid(form)
