from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index_page'),
    path('watcher/', views.lunchBot, name='lunch_page'),
]
