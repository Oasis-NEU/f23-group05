from django.shortcuts import render
from django.http import HttpResponse
import plotly.express as px

def home(request):
    return HttpResponse("Hello, Django!")

def webpageDunkin(request):
    print(request.build_absolute_uri()) #optional

    data=[[20, 30, 3, 5, 1, 25, 30, 50, 1, 5], 
          [3, 13, 20, 6, 20, 1, 60, 80, 30, 2], 
          [49, 40, 33, 97, 30, 60, 1, 5, 20, 3], 
          [3, 1, 9, 31, 2, 39, 37, 87, 88, 20], 
          [49, 92, 47, 55, 50, 30, 23, 20, 15, 40]]
    fig = px.imshow(data,
                    labels=dict(x="Time of Day", y="Day of Week", color="Customers"),
                    x=['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm'],
                    y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                )
    fig.update_xaxes(side="top")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', "paper_bgcolor": 'rgba(0,0,0,0)'})

    return render(
        request,
        'webpages/dunkin.html',
        context={'plot': fig.to_html(config={'displayModeBar': False}), 'plot2': fig.to_html(config={'displayModeBar': False})}
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