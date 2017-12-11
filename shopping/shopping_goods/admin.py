from django.contrib import admin
from .models import *


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle','isDelete']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','isDelete','gunit','gclick','gstock','grecommend','gdetail','gtype']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
# Register your models here.
