from django.contrib import admin
from django.urls import path
from blog.views import index
urlpatterns = [
    path('', index, name='index'),
]
