from django import forms
from django.contrib.auth import authenticate

from .models import Meal, Course

class MealForm(forms.Form):
    """ Formulario de registro de un almuerzo """
    entrada = forms.ModelChoiceField(
        queryset=Course.objects.filter_by_type('EN'),
        required=True,
    )

    primer_plato = forms.ModelChoiceField(
        queryset=Course.objects.filter_by_type('PP'),
        required=True,
    )

    postre = forms.ModelChoiceField(
        queryset=Course.objects.filter_by_type('PO'),
        required=True,
    )

    class Meta:
        model = Course
        fields = (
            'entrada', 
            'primer_plato', 
            'postre'
        )

    def clean_entrada(self):
        model_ids = Course.objects.filter_by_type('EN').values_list('id', flat=True)
        data_id = Course.objects.get(course_name=self.cleaned_data['entrada']).id
        if data_id not in model_ids:
            self.add_error('entrada', 'Debe seleccionar una entrada válida.')
        return self.cleaned_data['entrada']

    def clean_primer_plato(self):
        model_ids = Course.objects.filter_by_type('PP').values_list('id', flat=True)
        data_id = Course.objects.get(course_name=self.cleaned_data['primer_plato']).id
        if data_id not in model_ids:
            self.add_error('primer_plato', 'Debe seleccionar un primer plato válido.')
        return self.cleaned_data['primer_plato']

    def clean_postre(self):
        model_ids = Course.objects.filter_by_type('PO').values_list('id', flat=True)
        data_id = Course.objects.get(course_name=self.cleaned_data['postre']).id
        if data_id not in model_ids:
            self.add_error('postre', 'Debe seleccionar un postre válido.')
        return self.cleaned_data['postre']


class UpdateMealForm(forms.ModelForm, MealForm):
    """ Formulario de editar de un almuerzo """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mealInstance = kwargs['instance']
        # Set edit instance initial values
        self.fields['entrada'].initial = mealInstance.meal_courses.all()[2]
        self.fields['primer_plato'].initial = mealInstance.meal_courses.all()[1]
        self.fields['postre'].initial = mealInstance.meal_courses.all()[0]