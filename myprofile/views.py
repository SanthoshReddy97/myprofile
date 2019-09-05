from django.shortcuts import render
from django.http import HttpResponse
from .models import user
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        newUser = user(username= username, email= email, password= password1)
        newUser.save()
        return HttpResponse("deltails stored")

    else:
        return render(request, 'index.html')
    

    