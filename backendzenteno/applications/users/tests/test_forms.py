from django.test import SimpleTestCase, TestCase
from ..forms import RegisterForm, LoginForm
from ..models import User

class TestForms(TestCase):
    # Crear un usuario para el login y cambio de contraseña
    def setUp(self):
        self.user_login_test = User.objects.create_user(
            'login@gmail.com', 
            'pwlogin123',
            user_role = 1,
            user_name = 'login'
        )

    # Formulario de registro con datos correctos
    def test_register_form_valid_data(self):
        form = RegisterForm(data = {
            'user_name': 'user1',
            'user_email': 'user1@gmail.com',
            'user_role': '1',
            'password_first_time': 'user1password!#',
            'password_second_time': 'user1password!#',
        })
        self.assertTrue(form.is_valid())

    # Formulario de registro sin datos
    def test_register_form_invalid_data(self):
        form = RegisterForm(data = {})
        self.assertFalse(form.is_valid())

    # Formulario de login con datos correctos
    def test_login_form_valid_data(self):
        form = LoginForm(data = {
            'user_email': self.user_login_test.user_email,
            'user_password': 'pwlogin123'
        })
        self.assertTrue(form.is_valid())

    # Formulario de login con datos incorrectos
    def test_login_form_invalid_data(self):
        form = LoginForm(data = {
            'user_email': self.user_login_test.user_email + '1',
            'user_password': 'pwlogin123' + '1'
        })
        self.assertFalse(form.is_valid())