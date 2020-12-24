import datetime
from datetime import date

from django import forms
from django.contrib.auth import authenticate

from .models import Menu
from ..meals.models import Meal

class MenuForm(forms.Form):
    """ Formulario de registro de un almuerzo """
    menu_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            }
        ),
        required=True
    )


    menu_meals = forms.ModelMultipleChoiceField(
        queryset=Meal.objects.all(),
        required=True,
    )

    class Meta:
        model = Meal
        fields = (
            'menu_date', 
            'menu_meals', 
        )


    def clean_menu_date(self):
        form_date = self.cleaned_data['menu_date']
        if self.is_menu_to_past(form_date):
            self.add_error('menu_date', 'No se pueden crear menú para hoy o el pasado.')

        # Check si esta fecha ya tiene almuerzos
        if (Menu.objects.date_exists(form_date)):
            self.add_error('menu_date', 'Esta fecha ya tiene un menú.')

        return form_date


    def clean_menu_meals(self):
        form_meals = self.cleaned_data['menu_meals']
        meal_ids = self.get_ids_from_meals(form_meals)
        meal_model_ids = Meal.objects.all().values_list('id', flat=True)
        # Si estos almuerzos no existen en los almuerzos (tweaking de values en form)
        for meal_id in meal_ids:
            if meal_id not in meal_model_ids:
                self.add_error('menu_meals', 'Debe seleccionar un almuerzo válido.')
        return form_meals

    def get_ids_from_meals(self, meals):
        meal_ids = []
        for meal in meals:
            meal_ids.append(meal.id)
        return meal_ids

    # No se pueden crear menus hacia el pasado
    def is_menu_to_past(self, date):
        today = date.today()
        if date < today:
            return True
        return False


class MenuEditForm(forms.ModelForm, MenuForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        modelInstance = Menu.objects.get(menu_date = str(kwargs['instance']))
        # Set edit instance initial values
        self.fields['menu_date'].initial = kwargs['instance']
        self.fields['menu_meals'].initial = modelInstance.menu_meals.all()

    # Override de clean fecha de MenuForm
    def clean_menu_date(self):
        form_date = self.cleaned_data['menu_date']
        if self.is_menu_to_past(form_date):
            self.add_error('menu_date', 'No se puede editar este menú para hoy o el pasado.')

        initial_date = self.fields['menu_date'].initial
        # Si esta fecha es distinta que la inicial
        if not str(form_date) == str(initial_date):
            # Chequear que esta nueva fecha no tiene un menú
            if (Menu.objects.date_exists(form_date)):
                self.add_error('menu_date', 'Esta fecha ya tiene un menú.')

        return form_date

    
class SelectMenuForm(forms.Form):
    """ Formulario de selección de almuerzo del menú disponible """
    # Seleccionar almuerzo y un comentario opcional
    meals = forms.ModelChoiceField(
        queryset=None,
        required=True,
    )

    menu = forms.IntegerField()

    
    commentary = forms.CharField(
        max_length=300, 
        widget=forms.TextInput(
            attrs={
                'size':'40'
            }
        ),
        required=False
    )

    class Meta:
        fields = (
            'meals',
            'menu', 
            'commentary', 
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        today = date.today()
        modelInstance = Menu.objects.get(menu_date = str(today))
        # menu_meals Queryset
        self.fields['meals'].queryset = modelInstance.menu_meals.all()
        self.fields['menu'].initial = modelInstance.id

    def clean_meals(self):
        meal = self.cleaned_data['meals']
        today = date.today()

        is_valid = Menu.objects.is_valid_meal_for_today(meal.id, today)
        if is_valid:
            return meal
        else:
            self.add_error('meals', 'Seleccione un almuerzo válido.')

    def clean_commentary(self):
        commentary = self.cleaned_data['commentary']
        if len(commentary) > 300:
            self.add_error('commentary', 'Su comentario ha superado el límite.')
        elif len(commentary) == 0:
            return ''
        else:
            return commentary
