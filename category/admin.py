from django.contrib import admin
from .models import Subcategory, Category
# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Agro Almaty'
admin.site.register(Subcategory)
admin.site.register(Category)

