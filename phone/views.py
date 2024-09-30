from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from phone.forms import CreateUpdatePhoneForm
from phone.models import Phone, Brand


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
    template_name = 'phone/update_phone.html'
    form_class = CreateUpdatePhoneForm

    def setup(self, request, *args, **kwargs):
        self.phone_instance = get_object_or_404(Phone, id=kwargs.get('id'))
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.phone_instance)
        return render(request, 'phone/update_phone.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.phone_instance)

        if form.is_valid():
            updated_phone = form.save(commit=True)

            messages.success(request, 'Phone has been updated')
            return redirect('phone:index-page')

        messages.error(request, "form is invalid")
        # return redirect('phone:index-page')
        return render(request, 'phone/update_phone.html', {'form': form})


class DeletePhoneView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        """we don't delete phone, we just disActive it"""
        id = kwargs.get('id')
        phone = get_object_or_404(Phone, id=id)
        phone.is_active = False
        phone.save()
        messages.success(request, 'Phone has been deleted')
        return redirect('phone:index-page')
