from django.shortcuts import render

# Create your views here.
from .forms import PaymentForm
from .models import *

def payment_view(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, 'payment.html', context)