from django.shortcuts import render
from django.urls import reverse, reverse_lazy
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

from .models import Menu, Menu_meal, Menu_meal_user
from ..users.models import User

from ..apirest.slackapi import SlackAPIMethods


from .forms import (
    MenuForm,
    MenuEditForm,
    SelectMenuForm
)
# Create your views here.
# CRUD views menu
class MenuListView(LoginRequiredMixin, ListView):
    """ Listar todos los menus """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu.html'
    context_object_name = 'menu_list'
    success_url = reverse_lazy('menus_app:menu-list')

    def get_queryset(self):
        return Menu.objects.all()

    def post(self, request, *args, **kwargs):
        
        slack = SlackAPIMethods()
        slack_users = slack.send_empleados_direct_message()
        
        data = Menu.objects.all()
        return render(request, self.template_name, {'menu_list': data})


class MenuCreateView(LoginRequiredMixin, FormView):
    """ Crear un menu """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu_create.html'
    form_class = MenuForm
    success_url = reverse_lazy('menus_app:menu-list')

    def form_valid(self, form):
        menu = Menu(
            menu_date = form.cleaned_data['menu_date']
        )
        menu.save()
        for almuerzo in form.cleaned_data['menu_meals']:
            menu.menu_meals.add(almuerzo)

        return super(MenuCreateView, self).form_valid(form)


class MenuUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu_edit.html'
    model = Menu
    form_class = MenuEditForm
    success_url = reverse_lazy('menus_app:menu-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MenuDeleteView(LoginRequiredMixin, DeleteView):
    """ Borrar un menu """
    login_url = reverse_lazy('users_app:user-login')
    model = Menu
    success_url = reverse_lazy('menus_app:menu-list')

class MenuDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu_detail.html'
    model = Menu
    context_object_name = 'menu_detail'

class SelectMenuView(FormView):
    """ Crear una selección """
    template_name = 'menus/select_menu.html'
    form_class = SelectMenuForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user_uuid = self.kwargs['user_uuid']
        user_instance = User.objects.get(user_uuid = user_uuid)

        menu_id = form.cleaned_data['menu']
        meal = form.cleaned_data['meals']
        commentary = form.cleaned_data['commentary']
        menu_meal_instance = Menu_meal.objects.get(menu_id = menu_id, meal_id = meal.id)
        
        Menu_meal_user.objects.create(
            menu_meal_id = menu_meal_instance,
            user_id = user_instance,
            commentary = commentary
        )
        return super().form_valid(form)

class MyMenuMealsView(LoginRequiredMixin, ListView):
    """ Ver mi propia selección """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu_my_meals.html'
    context_object_name = 'menu_meal_user_list'
    success_url = reverse_lazy('menus_app:my-menu-meals')

    def get_queryset(self):
        menu_meal_user = Menu_meal_user.objects.filter(user_id = self.kwargs['pk'])
        return menu_meal_user


class MenuMealsListView(LoginRequiredMixin, ListView):
    """ Ver todas las selecciones """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu_list_selections.html'
    context_object_name = 'menu_meal_user_list'
    success_url = reverse_lazy('menus_app:menu-list-selections')

    def get_queryset(self):
        get_empleados = User.objects.filter(user_role = 1)
        menu_meal_user_list = []
        for empleado in get_empleados:
            menu_meal_user = Menu_meal_user.objects.filter(user_id = empleado.id)
            if menu_meal_user.exists():
                menu_meal_user_list.append(menu_meal_user)
        return menu_meal_user_list
