from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, ContactListView, OrderCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('create/', OrderCreateView.as_view(), name='create_order'),
]
