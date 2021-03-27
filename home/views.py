from django.shortcuts import render


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
