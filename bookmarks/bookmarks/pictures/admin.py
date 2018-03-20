from django.contrib import admin

# Register your models here.
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


admin.site.register(Picture, PictureAdmin)
