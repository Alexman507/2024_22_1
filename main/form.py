from django import forms

from main.models import Product, Contact, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        blacklist = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = self.cleaned_data['name'] + self.cleaned_data['description']

        for b_word in blacklist:
            if b_word in cleaned_data:
                raise forms.ValidationError(
                    'Нельзя использовать запретки (ладно, можно, но не все)')

        else:
            return self.cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
