from django.urls import path

from main.apps import MainConfig
from main.views import home, product_pk, pagination, contacts

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products/<int:pk>', product_pk, name='product_pk'),
    path('list_products/<int:per_page>/<int:page>/', pagination, name='pagination'),
    path('contacts/', contacts, name='contacts'),
]
