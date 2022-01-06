from django.contrib import admin
from django.urls import path
# from home import views
from . import views


urlpatterns = [   
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('ex1_sites/', views.ex1_sites, name='ex1_sites'),
    path('', views.index, name='index'),
    # path('removepunc', views.removepunc, name='rempun'),
    # path('capitalizefirst', views.capfirst, name='capfirst'),
    # path('newlineremove', views.newlineremove, name='newlineremove'),
    # path('spaceremove', views.spaceremove, name='spaceremove'),
    # path('charcount', views.charcount, name='charcount'),
    path('analyze', views.analyze, name='analyze')
]
