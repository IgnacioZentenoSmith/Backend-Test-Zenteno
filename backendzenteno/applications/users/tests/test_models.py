from django.test import TestCase
from ..models import User

class UserTestCase(TestCase):
    # Crear usuarios para testear
    def setUp(self):
        User.objects.create_user(
            'angelo@gmail.com', 
            'pwangelo123',
            user_role = 1,
            user_name = 'angelo'
        )

        User.objects.create_user(
            'rogelio@gmail.com', 
            'pwrogelio123',
            user_role = 2,
            user_name = 'rogelio'
        )

    # Verificar __str__ del modelo User
    def test_user_str(self):
        user1 = User.objects.get(user_email="angelo@gmail.com")
        user2 = User.objects.get(user_email="rogelio@gmail.com")
        self.assertEqual(str(user1), user1.user_name + user1.user_email)
        self.assertEqual(str(user2), user2.user_name + user2.user_email)



    
