from django.contrib import admin
from .models import Genre, Netflix


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class NetflixAdmin(admin.ModelAdmin):
    list_display = ("sub_genre", "link", "genre")


# Register your models here.
admin.site.register(Netflix, NetflixAdmin)
admin.site.register(Genre, GenreAdmin)
