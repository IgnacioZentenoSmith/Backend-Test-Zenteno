# Generated by Django 3.0.4 on 2020-12-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='meal_courses',
            field=models.ManyToManyField(to='meals.Course'),
        ),
        migrations.DeleteModel(
            name='Meal_courses',
        ),
    ]