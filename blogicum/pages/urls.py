from django.urls import path
from . import views

app_name = 'pages'  # Namespace для приложения pages

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
