from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from account.forms import UserRegistrationForm, UserLoginForm


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('phone:index-page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('phone:index-page')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                     form.cleaned_data['password'])

            messages.success(request, 'Account created for ' + form.cleaned_data['username'])
            return redirect('phone:index-page')
        return render(request, self.template_name, {'form': form, })


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('phone:index-page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in')
                return redirect('phone:index-page')
            messages.error(request, 'Invalid username or password')

        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You have been logged out')
            return redirect('account:register')


class UserPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'
    success_url = reverse_lazy('account:password-reset-done')  # in develop process it' not created yet
    email_template_name = 'account/password_reset_email.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy("account:password-reset-complete")  # todo : built it


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
