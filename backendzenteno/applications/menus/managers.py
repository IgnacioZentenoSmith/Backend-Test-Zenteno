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

    def is_valid_meal_for_today(self, meal_id, today):
        today_menu = self.get(menu_date = str(today))
        today_meals = today_menu.menu_meals.all()
        for today_meal in today_meals:
            if today_meal.id == meal_id:
                return True
        return False
class Menu_mealManager(models.Manager):
    """ Manager del modelo Menu_meal """

class Menu_meal_userManager(models.Manager):
    """ Manager del modelo Menu_meal_user """