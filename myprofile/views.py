from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core import serializers
from .models import user
import hashlib
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if (password1 == password2):  
            password1 = hashlib.sha256(str.encode(password1)).hexdigest()
            newUser = user(username= username, email= email, password= password1)
            newUser.save()
            return HttpResponse("deltails stored")
        else:
            messages.info(request, "password didnot match")
            return redirect("home")
    else:
        return render(request, 'index.html')
def getall(request):
    data = serializers.serialize("json", user.objects.all(), fields=('username', 'email'))
    return HttpResponse(data)

def newhome(request):
    return HttpResponse("Hello world")
    

    