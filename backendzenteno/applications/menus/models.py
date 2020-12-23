from django.db import models
from model_utils.models import TimeStampedModel

from .managers import MenuManager, Menu_mealManager

from ..meals.models import Meal

# Create your models here.
class Menu(TimeStampedModel):
    # Constants
    # Fields
    menu_date = models.DateField()
    menu_meals = models.ManyToManyField(Meal, through='Menu_meal')

    # Manager
    objects = MenuManager()

    # Standard methods
    def __str__(self):
	    return str(self.menu_date)

class Menu_meal(TimeStampedModel):
    # Constants
    # Fields
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)

    # Manager
    objects = Menu_mealManager()

    # Standard methods
    def __str__(self):
	    return self.menu_id + self.meal_id