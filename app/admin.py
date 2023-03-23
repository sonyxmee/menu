from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Menu


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Menu)

# class CategoryAdmin(TreeAdmin):
#     form = movenodeform_factory(Category)
#
#
# admin.site.register(Category, CategoryAdmin)