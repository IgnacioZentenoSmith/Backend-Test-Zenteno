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

from .models import Menu, Menu_meal

from .forms import (
    MenuForm,
    MenuEditForm
)

# Create your views here.
# CRUD views menu
class MenuListView(LoginRequiredMixin, ListView):
    """ Listar todos los menus """
    login_url = reverse_lazy('users_app:user-login')
    template_name = 'menus/menu.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Menu.objects.all()
    
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

# class MenuUpdateView(LoginRequiredMixin, UpdateView):
#     """ Editar un menu """
#     login_url = reverse_lazy('users_app:user-login')
#     template_name = 'menus/menu_edit.html'
#     model = Menu
#     form_class = MenuEditForm
#     success_url = reverse_lazy('menus_app:menu-list')

#     def form_valid(self, form):
#         print(form.instance.id, form.cleaned_data['fecha'])
#         Menu.objects.update_if_different_date(form.instance.id, form.cleaned_data['fecha'])
#         return super(MenuUpdateView, self).form_valid(form)

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
    