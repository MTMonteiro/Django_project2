from django.contrib import admin

from .models import Aps

@admin.register(Aps)
class ApsAdmin(admin.ModelAdmin):
    list_display = ('ap', 'modelo', 'canal', 'slug', 'criado', 'modificado', 'ativo')


