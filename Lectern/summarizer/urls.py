from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('lecture/<slug:slug>', views.lecture, name='lecture'),
    path('about', views.about, name='about')
]
