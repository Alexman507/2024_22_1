from django import forms

from main.models import Product, Contact


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        pass


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


# class VersionForm(forms.ModelForm):
#     class Meta:
#         model = Version
#         fields = '__all__'