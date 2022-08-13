from django.shortcuts import render
from requests import request
from . import models


def services(request):
    all_services = models.Services.objects.all()
    all_prices = models.Prices.objects.all()
    context = {
        'all_services': all_services,
        'all_prices': all_prices
    }
    
    return render(request, 'services/services.html', context=context)


def services_long_decription(request):
    all_services = models.Services.objects.all()
    context = {'all_services': all_services}
    return render(request, 'services/services_long_decription.html', context=context)


def contacts(request):
    return render(request, 'services/contacts.html')

