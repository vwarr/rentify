from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)