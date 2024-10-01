from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('password-reset/', views.UserPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('password-reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password-reset-complete'),

]
