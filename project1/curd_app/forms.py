from django import forms
from .models import ProductOrder


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"

        widgets = {
            "product_name": forms.TextInput(attrs={"class": "form-control"}),
            "product_price": forms.NumberInput(attrs={"class": "form-control"}),
            "product_quan": forms.Select(attrs={"class": "form-control"}),
            "delivery_address": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "payment_mode": forms.Select(attrs={"class": "form-control"})
        }
