from django import forms
from .models import *

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'amount',
            'method', #Card/Wallet
            #'Card ID',
            #'Wallet ID',
            'bank'
        ]