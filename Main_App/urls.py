from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # add page
    path('add/', views.add, name='add'),

]