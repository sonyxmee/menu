from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.main, name='main'),
    path('menu/<int:id_menu>/', views.get_short_menu, name='select_menu'),
    path('menu/<int:id_menu>/<int:id_cat>/', views.get_selected_category, name='select_cat'),
]
