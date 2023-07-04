from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from currency import models
from currency.forms import ContactsForm, RatesForm, SourcesForm


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


def contact_create(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contacts_table')

    form = ContactsForm()

    context = {
        'form': form,
    }
    return render(request, 'currency/contact_create.html', context)


def contact_update(request, pk):
    contact_to_update = get_object_or_404(models.Contacts, id=pk)
    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=contact_to_update)
        if form.is_valid():
            form.save()
            return redirect('contacts_table')
    form = ContactsForm(instance=contact_to_update)

    context = {
        'form': form,
        'id': pk
    }

    return render(request, 'currency/contact_update.html', context)


def contact_delete(request, pk):
    contact_to_delete = get_object_or_404(models.Contacts, id=pk)
    if request.method == 'GET':
        context = {
            'contact': contact_to_delete
        }
        return render(request, 'currency/contact_delete.html', context)
    elif request.method == 'POST':
        contact_to_delete.delete()
        return redirect('contacts_table')


def rate_create(request):
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rates_table')

    form = RatesForm()

    context = {
        'form': form,
    }
    return render(request, 'currency/rate_create.html', context)


def rate_update(request, pk):
    rate_to_update = get_object_or_404(models.Rates, id=pk)
    if request.method == 'POST':
        form = RatesForm(request.POST, instance=rate_to_update)
        if form.is_valid():
            form.save()
            return redirect('rates_table')
    form = RatesForm(instance=rate_to_update)

    context = {
        'form': form,
        'id': pk
    }

    return render(request, 'currency/rate_update.html', context)


def rate_delete(request, pk):
    rate_to_delete = get_object_or_404(models.Rates, id=pk)
    if request.method == 'GET':
        context = {
            'rate': rate_to_delete
        }
        return render(request, 'currency/rate_delete.html', context)
    elif request.method == 'POST':
        rate_to_delete.delete()
        return redirect('rates_table')


def sources_table(request):
    sources = models.Sources.objects.all()

    context = {'sources': sources}

    return render(request, 'currency/sources.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourcesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sources_table')

    form = SourcesForm()

    context = {
        'form': form,
    }
    return render(request, 'currency/source_create.html', context)


def source_update(request, pk):
    source_to_update = get_object_or_404(models.Sources, id=pk)
    if request.method == 'POST':
        form = SourcesForm(request.POST, instance=source_to_update)
        if form.is_valid():
            form.save()
            return redirect('sources_table')
    form = SourcesForm(instance=source_to_update)

    context = {
        'form': form,
        'id': pk
    }

    return render(request, 'currency/source_update.html', context)


def source_delete(request, pk):
    source_to_delete = get_object_or_404(models.Sources, id=pk)
    if request.method == 'GET':
        context = {
            'source': source_to_delete
        }
        return render(request, 'currency/source_delete.html', context)
    elif request.method == 'POST':
        source_to_delete.delete()
        return redirect('sources_table')
