from django.urls import path
from presenca import views


urlpatterns = [
    path('', views.home, name='home'),
]
