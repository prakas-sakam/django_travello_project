from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.name, name='name'),
    path('add', views.add,name='add')

]