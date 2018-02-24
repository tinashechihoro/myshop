from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,12)]

class CartAddProductForm(forms.Form):
    """
    CartAddProductForm
    """

    quantity = forms.TypeChoiceField(
                                    choices=PRODUCT_QUANTITY_CHOICES,
                                    coerce=int)
                                    