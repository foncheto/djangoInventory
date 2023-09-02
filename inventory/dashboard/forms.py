from django import forms
from .models import Product
from .models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]
