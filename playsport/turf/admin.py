from django.contrib import admin

from .models import *

# Register your models here.
# class AdminModel(admin.ModelAdmin):
#     list_display = ('id','photo','name','place','price')
#
# admin.site.register(Productmodel,AdminModel)

# class AdminModels(admin.ModelAdmin):
#     list_display = ('id','user', 'name', 'place', 'mobile_no')
# admin.site.register(RegisterForm, AdminModels)
admin.site.register(Productmodel),
admin.site.register(RegisterForm)