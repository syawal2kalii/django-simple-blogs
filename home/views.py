from django.shortcuts import render
from .forms import Users
from .models import article
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    context = {
        'title': 'blogs',
        'posts': [
            {
                'posted': 'syawal',
                'title': 'artikel 1'
            },
            {
                'posted': 'anu',
                'title': ' artikel 2'
            },
            {
                'posted': 'syawal',
                'title': ' artikel 3'
            }
        ]
    }
    return render(request, 'home.html', context)


def detail(request, id_article):
    context = {
        'id_article': id_article,
    }
    return render(request, 'detail.html', context)


def details(request, id_article, users_id):
    context = {
        'id_article': id_article,
        'users': users
    }
    return render(request, 'detail.html', context)


def adduser(request):
    if request.method == 'POST':
        print("post")
        User.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            # request.POST['first_name'],
            # request.POST['last_name'],
            email=request.POST['email']
        )
        return HttpResponseRedirect('/adduser/')
    return render(request, 'adduser.html', context={'form': Users()})
