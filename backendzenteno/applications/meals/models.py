from django.db import models

# Create your models here.
class Meal(models.Model):
    # Constants
    # Fields
    meal_name = models.CharField(max_length=150)

    # Manager
    # Standard methods
    def __str__(self):
	    return self.meal_name

class Meal_courses(models.Model):
    # Constants
    # Fields
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Manager

    #Meta
    class Meta:
        unique_together = ['meal_id', 'course_id']
    # Standard methods
    def __str__(self):
	    return 'id meal: ' + str(self.meal_id) + '; id course: ' + str(self.course_id)

class Course(models.Model):
    # Constants
    COURSE_TYPE_CHOICE = (
      	(1, 'Entrada'),
      	(2, 'Plato principal'),
        (3, 'Postre'),
    )

    # Fields
    course_name = models.CharField(max_length=50)
    course_type = models.PositiveSmallIntegerField(choices=COURSE_TYPE_CHOICE)

    # Manager

    #Meta
    class Meta:
        unique_together = ['course_name', 'course_type']

    # Standard methods
    def __str__(self):
	    return self.course_name + str(self.course_type)