from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from phone.forms import CreateUpdatePhoneForm


# Create your views here.


class indexView(View):
    def get(self, request):
        return render(request, 'phone/index.html')


class CreatePhoneView(LoginRequiredMixin, View):
    template_name = 'phone/create_phone.html'
    form_class = CreateUpdatePhoneForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'new phone has been created!')
            return redirect('phone:index-page')
        messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})


class UpdatePhoneView(LoginRequiredMixin, View):
    pass


class DeletePhoneView(LoginRequiredMixin, View):
    pass
