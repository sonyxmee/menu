from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from treebeard.mp_tree import MP_Node


# class Category(MP_Node):
#     name = models.CharField(max_length=30)
#
#     node_order_by = ['name']
#
#     def __str__(self):
#         return f"{self.pk}: {self.name}"
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

class Menu(models.Model):
    name_menu = models.CharField(max_length=30, unique=True, verbose_name='название меню')

    def __str__(self):
        return f"{self.name_menu}"

    def get_absolute_url(self):
        return reverse('menu')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(MPTTModel):
    name_category = models.CharField(max_length=30, unique=True, verbose_name='название категории')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menus')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return f"{self.name_category}"

    def get_absolute_url(self):
        return reverse('category')

    class MPTTMeta:
        order_insertion_by = ['name_category']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
