import os
from datetime import datetime

from django.conf import settings

from ..users.models import User

from rest_framework.authtoken.models import Token
from slacker import Slacker

class SlackAPIMethods():

    def __init__(self):
        self.slack = Slacker(settings.SLACK_BOT_USER_TOKEN)

    def get_slack_users(self):
        response = self.slack.users.list()
        slack_users = []
        # Iterar en el objeto
        for member in response.body['members']:
            # Verificar que existe la llave "email"
            if 'email' in member['profile'].keys():
                # Crear un diccionario con los datos relevantes
                user_data = {
                    'id': member['id'],
                    'email': member['profile']['email'],
                    'token': '',
                    'uuid': ''
                }
                slack_users.append(user_data)
        return slack_users

    def get_empleados_from_slack_users(self):
        user_emails = User.objects.get_empleados_emails()
        slack_users = self.get_slack_users()
        # Buscar aquellos usuarios de slack que son empleados
        for slack_user in slack_users:
            if slack_user['email'] not in user_emails:
                # Eliminar si no es un empleado o no existe en el sistema
                slack_users.remove(slack_user)
            else:
                # Si es un empleado, agregar su token
                user_instance = User.objects.get(user_email = slack_user['email'])
                slack_user['token'] = Token.objects.get(user=user_instance).key
                slack_user['uuid'] = str(user_instance.user_uuid)
        return slack_users

    def send_empleados_direct_message(self):
        empleados = self.get_empleados_from_slack_users()
        print(empleados)
        for empleado in empleados:
            msg = empleado['email'] + ' - ' + empleado['token'] + ' - ' + empleado['uuid']
            self.send_slack_message(empleado['id'], msg)

    def send_slack_message(self, channel='#general', message=''):
        self.slack.chat.post_message(channel, message)


