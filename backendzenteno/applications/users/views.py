from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Vistas genericas
from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView
)

# Vistas de formulario
from django.views.generic.edit import (
    FormView
)

# Formularios de autenticación
from .forms import (
    RegisterForm, 
    LoginForm
)

# Modelos
from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['user_email'],
            form.cleaned_data['password_first_time'],
            user_role = form.cleaned_data['user_role'],
            user_name = form.cleaned_data['user_name']
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            user_email=form.cleaned_data['user_email'],
            password=form.cleaned_data['user_password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    fields = ['user_name', 'user_role']

    login_url = reverse_lazy('users_app:user-login')

    def get_success_url(self):
          # capture 'pk' as user_id and pass it to 'reverse_lazy()' function
          current_user_id=self.kwargs['pk']
          return reverse_lazy('users_app:user-profile', kwargs={'pk': current_user_id})

    def form_valid(self, form):
        usuario = self.request.user
        usuario = form.save()
        return super(UserUpdateView, self).form_valid(form)

    