from django.shortcuts import render

from .models import Category, Menu


def main(request):
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, template_name='app/main.html', context=context)


def get_short_menu(request, id_menu):
    cat = Category.objects.filter(menu=id_menu)
    print(cat)
    context = {'category': cat, 'id_menu': id_menu}
    return render(request, template_name='app/short_menu.html', context=context)


def get_selected_category(request, id_menu, id_cat):
    cat = Category.objects.filter(menu=id_menu)
    context = {'category': cat, 'id': id_cat, 'id_menu': id_menu}
    return render(request, template_name='app/selected_cat.html', context=context)
