from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Message
from .forms import MessageForm
from .forms import forms
# Create your views here.
def main(request):
    return render(request, 'kimono/main.html',{})

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
            ("2018", "2018"),
            ("2019", "2019"),
            ("2020", "2020"),
            ("2021", "2021"),
            ("2022", "2022"),
            ("2023", "2023"),
            ("2024", "2024"),
            ("2025", "2025"),
            ("2026", "2026"),
            ("2027", "2027"),
            ("2028", "2028"),
            ("2029", "2029"),
            ("2030", "2030"),
    ]
    form.fields["hotel"].choices = [
           ("another","another"),
           ("A hotel","A hotel"),
           ("B hotel","B hotel"),
           ("C hotel","C hotel"),
           ("D hotel","D hotel"),
           ("E hotel","E hotel"),
           ("F hotel","F hotel"),
           ("G hotel","G hotel"),
           ("H hotel","H hotel"),
    ]
    form.fields["kimono_select"].choices = [
           ("No.1","No1"),
           ("No.2","No.2"),
           ("No.3","No.3"),
           ("No.4","No.4"),
           ("No.5","No.5"),
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
