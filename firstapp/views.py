from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .models import db, dbForm

def about(request):
    if request.user.is_authenticated:
        DbForm = dbForm()
        Db = db.objects.all()
        person = request.user.get_username()
        return render(request, 'about.html', {'person':person, 'DbForm':DbForm, 'Db':Db})
    else:
        return redirect('login')


class Logout(LogoutView):
    template_name = 'registration\Logout.html'
    

class index(LoginView, AuthenticationForm):
    extra_context = {
        'person':AuthenticationForm
    }
    template_name = 'registration\login.html'
    
def ADD(request):
    Db = db()
    Db.person = request.user.username
    Db.message = request.POST.get('content')
    Db.save()
    return HttpResponseRedirect('/about/')