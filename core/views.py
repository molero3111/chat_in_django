from django.contrib.auth import login
from django.shortcuts import render, redirect

from core.forms import SignUpForm


def frontpage(request):
    return render(request, 'frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('rooms')
    else:
        # If it's not a POST request, or the form is invalid, include the form with errors in the context
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
