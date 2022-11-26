from django.urls import path, include
from . import views

urlpatterns = [
    path('logs/', views.logs, name = 'logs'),
    path('upload/', views.upload, name = 'upload'),
    path('', views.home, name = 'home'),
    path('result/', views.result, name = 'result'),
    path('test/',views.test, name = 'test')
]
