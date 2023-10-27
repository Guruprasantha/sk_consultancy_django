from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('home/', views.back,name='home'),
    path('elec/', views.elec,name='elec'),
    path('plum/', views.plum,name='plum'),
    path('ele/',views.ele,name='ele'),
    path('plumi/',views.plumi,name='plumi')
    
]