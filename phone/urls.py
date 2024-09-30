from django.urls import path
from phone import views

app_name = 'phone'
urlpatterns = [
    path('', views.indexView.as_view(), name='index-page'),
    path('create-phone/', views.CreatePhoneView.as_view(), name='create-phone'),
    path('update-phone/<int:id>', views.UpdatePhoneView.as_view(), name='update-phone'),
    path('delete-phone/<int:id>', views.DeletePhoneView.as_view(), name='delete-phone'),
]
