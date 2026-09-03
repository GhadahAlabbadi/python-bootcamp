from django.shortcuts import render

def checkout(request):
    return render(request, 'payments/checkout.html')

def receipt(request):
    return render(request, 'payments/receipt.html')