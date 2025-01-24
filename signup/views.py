from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import SignupForm


def landing_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'signup/thank_you.html')
    else:
        form = SignupForm()
    return render(request, 'signup/landing_page.html', {'form': form})
