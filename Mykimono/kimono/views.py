from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Message
from .forms import MessageForm
from .forms import forms
# Create your views here.
def index(request):
    form = MessageForm(request.POST or None)
    form.fields["pay_type"].choices = [
            ("JCB", "JCB"),
            ("VISA", "VISA"),
            ("MASTERCARD", "MASTERCARD"),
            ("Local PayMent", "Local PayMent"),
    ]
    d = {
    'messages':Message.objects.all(),
    }
    return render(request, 'kimono/index.html', d)


def add(request):
    form = MessageForm(request.POST or None)
    form.fields["pay_type"].choices = [
            ("JCB", "JCB"),
            ("VISA", "VISA"),
            ("MASTERCARD", "MASTERCARD"),
            ("Local PayMent", "Local PayMent"),
    ]
    form.fields["expiry_date"].choices = [
            ("-", "-"),
            ("01", "01"),
            ("02", "02"),
            ("03", "03"),
            ("04", "04"),
            ("05", "05"),
            ("06", "06"),
            ("07", "07"),
            ("08", "08"),
            ("09", "09"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
    ]
    form.fields["expiry_year"].choices = [
            ("-", "-"),
            ("01", "01"),
            ("02", "02"),
            ("03", "03"),
            ("04", "04"),
            ("05", "05"),
            ("06", "06"),
            ("07", "07"),
            ("08", "08"),
            ("09", "09"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
    ]
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('index')

    d = {
        'form': form,
    }
    return render(request, 'kimono/edit.html', d)


def edit(request, editing_id):
    message = get_object_or_404(Message, id=editing_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.message = form.cleaned_data['message']
            message.save()
            return redirect('index')
    else:
        form = MessageForm({'message': message.message})
    d = {
        'form': form,
    }
    return render(request, 'kimono/edit.html', d)

@require_POST
def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('index')
