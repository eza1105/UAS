from django.contrib import admin
from MSY.models import *

# Register your models here.
class dataikanadmin(admin.ModelAdmin):
    list_display   = ['jenis_usaha','provinsi', 'jenis_ikan', 'tahun', 'trip', 'ton']
    search_fields  = ['jenis_usaha','provinsi', 'jenis_ikan', 'tahun', 'trip', 'ton']
    list_per_page  : 5

admin.site.register(dataikan)