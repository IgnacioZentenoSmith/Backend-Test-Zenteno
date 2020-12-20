from django import forms
from django.contrib.auth import authenticate

from .models import User

# Formularios encargados de la autenticación de usuarios (Register, Login, Recuperar password)
class RegisterForm(forms.ModelForm):
    """ Formulario de registro de un usuario """
    password_first_time = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password_second_time = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """ Meta definition de formulario de registro """
        model = User
        fields = (
            'user_name',
            'user_email',
            'user_role',
        )

        widgets = {
            'user_email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ej: pablo@gmail.com'
                }
            )
        }
    # Asegurar que las contraseñas son iguales, de lo contrario enviar error
    def clean_password_second_time(self):
        if self.cleaned_data['password_first_time'] != self.cleaned_data['password_second_time']:
            self.add_error('password_second_time', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    user_email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electrónico',
            }
        )
    )
    user_password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        user_email = self.cleaned_data['user_email']
        user_password = self.cleaned_data['user_password']

        # Si no se ha podido autenticar, error de credenciales
        if not authenticate(user_email=user_email, password=user_password):
            raise forms.ValidationError('Una o más credenciales son incorrectas.')
        
        return self.cleaned_data