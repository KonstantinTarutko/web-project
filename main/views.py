import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, SecondForm
from django.core.mail import send_mail


def index(request):
    data = {
        'title': 'Main page'
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sending_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                # 'problem': form.cleaned_data['problem'],
                'message': form.cleaned_data['message'],
            }

            send_mail(
                'first form',
                json.dumps(data),
                't7est567@yandex.ru',
                ['tarutko.konstantin@yandex.ru'],
                fail_silently=False
            )

            return redirect('/contacts')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request,
                  'main/index.html',
                  context)


def sending_second_form(request):
    if request.method == 'POST':
        form = SecondForm(request.POST)

        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message']
            }

            send_mail(
                'second form',
                json.dumps(data),
                't7est567@yandex.ru',
                ['tarutko.konstantin@yandex.ru'],
                fail_silently=False
            )

            return redirect('main')

    else:
        form = SecondForm()

    context = {'form': form}
    return render(request,
                  'main/contacts.html',
                  context)
