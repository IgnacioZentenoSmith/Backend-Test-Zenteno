from django.db import models

# Create your models here.
class Menu(models.Model):
    # Constants
    # Fields
    menu_date = models.DateField()

    # Manager
    # Standard methods
    def __str__(self):
	    return 'Menu de fecha: ' + self.menu_date

class Menu_meal(models.Model):
    # Constants
    # Fields
    menu_id = models.ForeignKey()
    meal_id = models.ForeignKey()

    # Manager
    # Standard methods
    def __str__(self):
	    return 'id menu: ' + str(self.menu_id) + '; id meal: ' + str(self.meal_id)