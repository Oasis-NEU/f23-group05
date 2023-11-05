from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def webpageDunkin(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'webpages/dunkin.html',
        
    )

def webpageStarbucks(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'webpages/starbucks.html',
        
    )

def webpageHome(request):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'webpages/homepage.html',
        
    )