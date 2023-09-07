# Connecting sthe data base with the django admin panel

from .models import Movies, Users
from django.contrib import admin


admin.site.register(Movies)
admin.site.register(Users)
