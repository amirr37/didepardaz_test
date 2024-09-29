from django.urls import path
from phone import views

urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
]
