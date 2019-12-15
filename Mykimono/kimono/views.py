from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'kimono/index.html', {})


def add(request):
    return render(request, 'kimono/edit.html', {})


def edit(request, editing_id):
    return render(request, 'kimono/edit.html', {})


def delete(request):
    return HttpResponse('Delete')
