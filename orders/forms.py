from django import forms
from .models import Order

class OrderCreateForm(forms.Form):
    class Meta:
        model = Order
        fields = ['first_name','late_name','email','address',
                    'postal_code','city']