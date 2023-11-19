from django.shortcuts import render
from django.http import HttpResponse
import plotly.express as px

def home(request):
    return HttpResponse("Hello, Django!")

def webpageDunkin(request):
    print(request.build_absolute_uri()) #optional

    data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20], [2, 39, 37, 87, 88]]
    fig = px.imshow(data,
                    labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    y=['12pm', '1pm', '2pm', '3pm'],
                )
    fig.update_xaxes(side="top")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', "paper_bgcolor": 'rgba(0,0,0,0)'})

    return render(
        request,
        'webpages/dunkin.html',
        context={'plot': fig.to_html(config={'displayModeBar': False})}
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