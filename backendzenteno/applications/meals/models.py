from django.db import models
from model_utils.models import TimeStampedModel

from .managers import MealManager, CourseManager

# Create your models here.
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
        return self.course_name

class Meal(TimeStampedModel):
    # Constants
    # Fields
    meal_courses = models.ManyToManyField(Course)

    # Manager
    objects = MealManager()

    # Standard methods
    def __str__(self):
        meal_courses = ", ".join(str(courses) for courses in self.meal_courses.all())
        return "{}: {}".format(self.id ,meal_courses)