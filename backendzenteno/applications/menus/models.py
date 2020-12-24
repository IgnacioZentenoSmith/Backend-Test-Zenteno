from django.db import models
from model_utils.models import TimeStampedModel

from .managers import MenuManager, Menu_mealManager, Menu_meal_userManager

from ..meals.models import Meal
from ..users.models import User

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
	    return str(self.menu_id) + str(self.meal_id)

class Menu_meal_user(TimeStampedModel):
    # Constants
    # Fields
    menu_meal_id = models.ForeignKey(Menu_meal, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    commentary = models.TextField(blank=True)

    # Manager
    objects = Menu_meal_userManager()

    # Meta
    class Meta:
        unique_together = ['menu_meal_id', 'user_id']

    # Standard methods
    def __str__(self):
	    return str(self.menu_meal_id) + str(self.user_id)