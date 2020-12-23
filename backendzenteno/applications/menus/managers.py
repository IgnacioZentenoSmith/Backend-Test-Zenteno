from django.db import models
from django.db.models import Q


class MenuManager(models.Manager):
    """ Manager del modelo Menu """
    def date_exists(self, date):
        query_result = self.filter(menu_date = date).exists()
        return query_result

    def update_if_different_date(self, menu_id, date):
        menu = self.get(id = menu_id)
        menu.menu_date = date
        menu.save()

class Menu_mealManager(models.Manager):
    """ Manager del modelo Menu_meal """