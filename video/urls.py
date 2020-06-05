from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='asl-home'),
    # path('about/', views.about, name='asl-about'),
]
