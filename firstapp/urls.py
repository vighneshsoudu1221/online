from django.urls import path
from.import views

urlpatterns=[
    path("",views.display),
    path("hi/",views.show),
    path("index/",views.send),
    path("calculator/", views.calculator),
    path("mtable/",views.mtable),
    
]