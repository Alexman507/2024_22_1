from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Product, Category, Contact, Order


# Create your views here.

class ProductListView(ListView):
    model = Product


# def home(request):
#     products_list = Product.objects.all()
#     category_list = Category.objects.all()
#     # Product.objects.all().delete()
#     # Category.objects.all().delete()
#     #
#     context = {
#         'object_list': products_list,
#         'title': 'Каталог'
#     }
#
#     return render(request, 'main/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


# def product_pk(request, pk, page=None, per_page=None):
#     obj = get_object_or_404(Product, pk=pk)
#     context = {
#         "object": obj,
#         "pagination": bool(per_page),
#         "per_page": per_page,
#         "page": page
#     }
#
#     return render(request, 'main/product_detail.html', context)


def pagination(request, page, per_page):
    len_product = len(Product.objects.all())
    if len_product % per_page != 0:
        page_count = [x + 1 for x in range((len_product // per_page) + 1)]
    else:
        page_count = [x + 1 for x in range((len_product // per_page))]

    product_list = Product.objects.all()[per_page * (page - 1): per_page * page]

    context = {
        "product_list": product_list,
        "page": page,
        "per_page": per_page,
        "page_count": page_count
    }

    return render(request, 'main/per_page.html', context)


def contacts(request):
    number = len(Contact.objects.all())
    if number > 5:
        contacts_list = Contact.objects.all()[number - 5: number + 1]
    else:
        contacts_list = Contact.objects.all()

    context = {
        'object_list': contacts_list,
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        info = {'created_at': (datetime.now()).strftime('%Y-%m-%dT%H:%M'),
                'name': name, 'phone': phone, 'message': message
                }

        Order.objects.create(**info)

    return render(request, 'main/contacts.html', context)

# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     return render(request, 'main/index.html')
