from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.edit import FormView

from .models import Meal, Course

from .forms import (
    MealForm,
    UpdateMealForm
)

# Create your views here.
# CRUD views meal
class MealListView(LoginRequiredMixin, ListView):
    """ Listar todos los almuerzos """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/meal.html'
    context_object_name = 'meal_list'

    def get_queryset(self):
        return Meal.objects.all()
    
class MealCreateView(LoginRequiredMixin, FormView):
    """ Crear un almuerzo """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/meal_create.html'
    form_class = MealForm
    
    success_url = reverse_lazy('meals_app:meal-list')
    

    def form_valid(self, form):
        #
        meal = Meal()
        meal.save()
        
        entrada = Course.objects.get(course_name=form.cleaned_data['entrada'])
        primer_plato = Course.objects.get(course_name=form.cleaned_data['primer_plato'])
        postre = Course.objects.get(course_name=form.cleaned_data['postre'])
        meal.meal_courses.add(entrada, primer_plato, postre)

        return super(MealCreateView, self).form_valid(form)

class MealUpdateView(LoginRequiredMixin, UpdateView):
    """ Editar un almuerzo """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/meal_edit.html'
    model = Meal
    form_class = UpdateMealForm
    success_url = reverse_lazy('meals_app:meal-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Encontrar la instancia
        meal = Meal.objects.get(id = self.kwargs['pk'])
        # Limpiar todas las many to many de esta instancia
        meal.meal_courses.clear()
        # Buscar los nuevos platos
        entrada = Course.objects.get(course_name=form.cleaned_data['entrada'])
        primer_plato = Course.objects.get(course_name=form.cleaned_data['primer_plato'])
        postre = Course.objects.get(course_name=form.cleaned_data['postre'])
        # Agregar los nuevos platos
        meal.meal_courses.add(entrada, primer_plato, postre)
        return super().form_valid(form)

class MealDeleteView(LoginRequiredMixin, DeleteView):
    """ Borrar un almuerzo """
    login_url = reverse_lazy('users_app:user-login')
    model = Meal
    success_url = reverse_lazy('meals_app:meal-list')

# CRUD views course
class CourseListView(LoginRequiredMixin, ListView):
    """ Listar todos los platos """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/course.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()

class CourseCreateView(LoginRequiredMixin, CreateView):
    """ Crear un plato """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/course_create.html'
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('meals_app:course-list')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    """ Editar un plato """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'meals/course_edit.html'
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('meals_app:course-list')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    """ Borrar un plato """
    login_url = reverse_lazy('users_app:user-login')
    model = Course
    success_url = reverse_lazy('meals_app:course-list')
