from django.contrib import admin
from .models import Vaca, Lote

# Register your models here.

class VacasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class LotesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Vaca, VacasAdmin)
admin.site.register(Lote, LotesAdmin)