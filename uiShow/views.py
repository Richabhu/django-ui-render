from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.shortcuts import render


def firstpage(request):
    # return HttpResponse('homepage')
    return render(request, 'first.html')


def secpage(request):
    # return HttpResponse("about")
    return render(request, 'secpage.html')
