from django.shortcuts import render
from django.http import JsonResponse
from currency import models
# import json


def home_view(request):
    return render(request, 'currency/index.html')


def contacts_json(request):
    data = {}

    contacts = models.Contacts.objects.all()
    if contacts:
        for ind, contact in enumerate(contacts, start=1):
            data[ind] = {
                'id': contact.id,
                'email_from': contact.email_from,
                'subject': contact.subject,
                'message': contact.message
            }

    return JsonResponse(data)


def contacts_table(request):
    contacts = models.Contacts.objects.all()

    context = {'contacts': contacts}

    return render(request, 'currency/contacts.html', context)


def rates_json(request):
    data = {}

    rates = models.Rates.objects.all()
    if rates:
        for ind, rate in enumerate(rates, start=1):
            data[ind] = {
                'id': rate.id,
                'currency': rate.currency,
                'buy': rate.buy,
                'sell': rate.sell,
                'source': rate.source,
                'created': rate.created
            }

    return JsonResponse(data)


def rates_table(request):
    rates = models.Rates.objects.all()

    context = {'rates': rates}

    return render(request, 'currency/rates.html', context)


def create_contact(request):
    pass