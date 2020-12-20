from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import UserRegisterView, LoginUser, LogoutView, UserUpdateView


class TestsUrlsResolving(SimpleTestCase):
    # URL de registro
    def test_register_url_resolves(self):
        url = reverse('users_app:user-register')
        self.assertEquals(resolve(url).func.view_class, UserRegisterView)

    # URL de login
    def test_login_url_resolves(self):
        url = reverse('users_app:user-login')
        self.assertEquals(resolve(url).func.view_class, LoginUser)

    # URL de logout
    def test_logout_url_resolves(self):
        url = reverse('users_app:user-logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)
        
    # URL del perfil de usuario
    def test_profile_url_resolves(self):
        url = reverse('users_app:user-profile', args=['pk'])
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)