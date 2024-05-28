from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, pagination, contacts

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('list_products/<int:per_page>/<int:page>/', pagination, name='pagination'),
    path('contacts/', contacts, name='contacts'),
]
