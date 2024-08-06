from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user in
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
