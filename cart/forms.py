from django import forms


from .models import CartCheckout


class CartCheckoutForm(forms.ModelForm):
    class Meta:
        model = CartCheckout
        fields = ['email', 'battletag', 'cart_items']

