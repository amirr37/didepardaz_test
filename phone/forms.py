from django import forms

from phone.models import Phone


class CreateUpdatePhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['model', 'brand', 'price', 'color', 'screen_size', 'in_stock', 'origin_country']
