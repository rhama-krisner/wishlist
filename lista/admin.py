from django.contrib import admin
from lista.models import ListaModel

class ListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'adquirido', 'imagem')
    list_display_links = ('id', 'produto')
    search_fields = ('id', 'produto', 'adquirido')
    list_per_page = 10

admin.site.register(ListaModel, ListaAdmin)