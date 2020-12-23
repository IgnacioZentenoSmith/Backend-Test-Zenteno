from django.urls import path
from . import views

app_name = "meals_app"

urlpatterns = [
    # CRUD urls meal
    path(
        'meals/meal', 
        views.MealListView.as_view(),
        name='meal-list',
    ),
    path(
        'meals/meal_create', 
        views.MealCreateView.as_view(),
        name='meal-create',
    ),
    path(
        'meals/meal_edit/<pk>', 
        views.MealUpdateView.as_view(),
        name='meal-edit',
    ),
    path(
        'meals/meal_delete/<pk>', 
        views.MealDeleteView.as_view(),
        name='meal-delete',
    ),
    # CRUD urls course
    path(
        'meals/course', 
        views.CourseListView.as_view(),
        name='course-list',
    ),
    path(
        'meals/course_create', 
        views.CourseCreateView.as_view(),
        name='course-create',
    ),
    path(
        'meals/course_edit/<pk>', 
        views.CourseUpdateView.as_view(),
        name='course-edit',
    ),
    path(
        'meals/course_delete/<pk>', 
        views.CourseDeleteView.as_view(),
        name='course-delete',
    ),
]