from django.urls import path
from phone import views

app_name = 'phone'
urlpatterns = [
    path('', views.indexView.as_view(), name='index-page'),
]
