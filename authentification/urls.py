from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    # path('', views.RegisterCreateView.as_view(), name='register'),
    path('thanks/', views.ThankyouView.as_view(), name='thanks'),
]