from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = "Gabi"

    args = {'myName': name}
    return render(request, 'accounts/login.html', args)
