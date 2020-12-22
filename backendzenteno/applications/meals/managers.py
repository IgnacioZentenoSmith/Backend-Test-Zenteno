from django.db import models
from django.db.models import Q


class MealManager(models.Manager):
    """ Manager del modelo Meal """
    def filter_by_name(self, name):
        query_result = self.filter(meal_name__icontains = name).order_by('meal_name')
        return query_result

class CourseManager(models.Manager):
    """ Manager del modelo Course """
    def filter_by_name(self, name):
        query_result = self.filter(course_name__icontains = name).order_by('course_name')
        return query_result