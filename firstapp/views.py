from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views import generic
from .models import db, dbForm
import os

def about(request):
    if request.user.is_authenticated:
        DbForm = dbForm()
        Db = db.objects.all()
        person = request.user.get_username()
        return render(request, 'about.html', {'person':person, 'DbForm':DbForm, 'Db':Db})
    else:
        return redirect('login')


class Logout(LogoutView):
    template_name = os.path.join('..', 'templates', 'reqistration', 'logout.html')
    

class index(LoginView, AuthenticationForm):
    extra_context = {
        'person':AuthenticationForm
    }
    template_name = os.path.join('..', 'templates', 'registration', 'login.html')


class signup(generic.CreateView):
    form_class = UserCreationForm
    template_name = os.path.join('..', 'templates', 'index.html')
    success_url = '/'


def ADD(request):
    Db = db()
    Db.person = request.user.username
    Db.message = request.POST.get('content')
    Db.save()
    return HttpResponseRedirect('/about/')