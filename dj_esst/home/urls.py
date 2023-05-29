from django.urls import path

# import views from the current directory
from . import views 

urlpatterns = [
    path('', views.home),
    path('authorized/', views.authorized)
    ]
