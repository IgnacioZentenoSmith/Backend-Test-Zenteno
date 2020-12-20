from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from ..views import UserRegisterView, LoginUser, LogoutView, UserUpdateView
from ..models import User
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.view_urls = {
            'register_url': reverse('users_app:user-register'),
            'login_url': reverse('users_app:user-login'),
            'logout_url': reverse('users_app:user-logout'),
            'user_update_url': reverse('users_app:user-profile', args=['pk']),
        }
        self.view_templates = {
            'register_template': 'users/register.html',
            'login_template': 'users/login.html',
            'logout_template': 'users/logout.html',
            'user_update_template': 'users/profile.html',
        }

    # GET views
    def test_user_register_GET(self):
        response = self.client.get(self.view_urls['register_url'])
        # Status OK
        self.assertEquals(response.status_code, 200)
        # Trae el template correcto
        self.assertTemplateUsed(response, self.view_templates['register_template'])

    def test_user_login_GET(self):
        response = self.client.get(self.view_urls['login_url'])
        # Status OK
        self.assertEquals(response.status_code, 200)
        # Trae el template correcto
        self.assertTemplateUsed(response, self.view_templates['login_template'])

    def test_user_logout_GET(self):
        response = self.client.get(self.view_urls['logout_url'])
        # Status URL Redirection
        self.assertEquals(response.status_code, 302)
        # No trae el template debido a redirección
        self.assertTemplateNotUsed(response, self.view_templates['logout_template'])

    def test_user_profile_GET(self):
        response = self.client.get(self.view_urls['user_update_url'])
        # Status URL Redirection
        self.assertEquals(response.status_code, 302)
        # No trae el template debido a redirección
        self.assertTemplateNotUsed(response, self.view_templates['user_update_template'])
