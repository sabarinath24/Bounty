from django.shortcuts import render, redirect
from .forms import DeedForm
from .models import Deed

def create_deed(request):
    if request.method == 'POST':
        form = DeedForm(request.POST)
        if form.is_valid():
            deed = form.save(commit=False)
            deed.owner = request.user
            deed.save()
            return redirect('deed_list')
    else:
        form = DeedForm()
    return render(request, 'deeds/create_deed.html', {'form': form})

def deed_list(request):
    deeds = Deed.objects.filter(owner=request.user)
    return render(request, 'deeds/deed_list.html', {'deeds': deeds})
