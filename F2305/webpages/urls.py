from django.urls import path
from webpages import views

urlpatterns = [
    path("dunkin", views.webpageDunkin, name="dunkin"),
    path("starbucks", views.webpageStarbucks, name="starbucks"),
    path("", views.webpageHome, name="home"),
    #path("", views.home, name="empty"),
]