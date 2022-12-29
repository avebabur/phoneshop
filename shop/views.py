from django.shortcuts import render, redirect
from .models import Phone, Rubric
from .forms import PhoneForm

def main_page(request):
    phones = Phone.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'phones': phones,
        'rubrics': rubrics
    }
    return render(request, 'shop/main_page.html', context)


def by_rubric(request, rubric_id):
    phones = Phone.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {
        'phones': phones,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'shop/by_rubric.html', context)

def create(request):
    form = PhoneForm()
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    context = {
        'form': form
    }
    return render(request,'shop/create.html', context)

def update(request, pk):
    phone = Phone.objects.get(id=pk)
    form = PhoneForm(instance=phone)
    if request.method == 'POST':
        form = PhoneForm(request.POST, instance=phone, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    context = {
        'form': form
    }
    return render(request, 'shop/update.html', context)

def delete(request, pk):
    phone = Phone.objects.get(id=pk)
    phone.delete()
    return redirect('/shop/')