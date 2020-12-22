from django.db import models

from model_utils.models import TimeStampedModel

from .managers import MealManager, CourseManager

# Create your models here.
class Meal(TimeStampedModel):
    # Constants
    # Fields
    meal_name = models.CharField(max_length=150)

    # Manager
    objects = MealManager()

    # Standard methods
    def __str__(self):
	    return self.meal_name

class Course(TimeStampedModel):
    # Constants
    ENTRADA = 'EN'
    PLATO_PRINCIPAL = 'PP'
    POSTRE = 'PO'
    COURSE_TYPE_CHOICE = [
        (ENTRADA, 'Entrada'),
        (PLATO_PRINCIPAL, 'Plato principal'),
        (POSTRE, 'Postre'),

    ]

    # Fields
    course_name = models.CharField(max_length=50)
    course_type = models.CharField(
        max_length=2,
        choices=COURSE_TYPE_CHOICE
    )

    # Manager
    objects = CourseManager()

    #Meta
    class Meta:
        unique_together = ['course_name', 'course_type']

    # Standard methods
    def __str__(self):
	    return self.course_name + self.course_type

class Meal_courses(TimeStampedModel):
    # Constants
    # Fields
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Manager

    #Meta
    class Meta:
        unique_together = ('meal_id', 'course_id')

    # Standard methods
    def __str__(self):
	    return 'id meal: ' + str(self.meal_id) + '; id course: ' + str(self.course_id)