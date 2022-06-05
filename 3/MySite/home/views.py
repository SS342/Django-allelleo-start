from django.shortcuts import render


def home(requests):
    return render(request=requests, template_name='home.html')
