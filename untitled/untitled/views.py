from __future__ import unicode_literals
from django.shortcuts import render
from hwapp.models import City
from django.http import HttpResponse


def hello(request):
    # return HttpResponse("HELLOWROLD")
    City = City.objects.all()
    return render(request, 'student.html', {'City': City})


def runoob(request):
    context = {}
    # context['hello'] = 'hello wrold'
    # context['views_name'] = '1加油'
    context = {"vies_dict": "今天下雨"}
    return render(request, 'runoob.html', {"context": context})
