from django.shortcuts import render


def simplemvt(request):
    return render(request, 'index.html')
