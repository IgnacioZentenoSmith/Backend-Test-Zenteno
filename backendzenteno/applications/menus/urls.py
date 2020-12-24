from django.urls import path
from . import views

app_name = "menus_app"

urlpatterns = [
    # CRUD urls menu
    path(
        'menus/menu', 
        views.MenuListView.as_view(),
        name='menu-list',
    ),
    path(
        'menus/menu_create', 
        views.MenuCreateView.as_view(),
        name='menu-create',
    ),
    path(
        'menus/menu_edit/<pk>', 
        views.MenuUpdateView.as_view(),
        name='menu-edit',
    ),
    path(
        'menus/menu_delete/<pk>', 
        views.MenuDeleteView.as_view(),
        name='menu-delete',
    ),
    path(
        'menus/menu_detail/<pk>', 
        views.MenuDetailView.as_view(),
        name='menu-detail',
    ),
    path(
        'menus/select_menu/<uuid:user_uuid>', 
        views.SelectMenuView.as_view(),
        name='select-menu',
    ),
    path(
        'menus/my_menu_meals/<pk>', 
        views.MyMenuMealsView.as_view(),
        name='my-menu-meals',
    ),

]