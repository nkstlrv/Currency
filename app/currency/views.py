from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from currency import models
# import json


def home_view(request):
    return render(request, 'currency/index.html')


def contactus_list(request):
    data = {}

    contacts = models.ContactUs.objects.all()
    if contacts:
        for ind, contact in enumerate(contacts, start=1):
            data[ind] = {
                'id': contact.id,
                'email_from': contact.email_from,
                'subject': contact.subject,
                'message': contact.message
            }

    return JsonResponse(data)
