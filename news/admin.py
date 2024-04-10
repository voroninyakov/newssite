from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'views']
    search_fields = ['title', 'text']

admin.site.register(Reaction)
admin.site.register(Tag)