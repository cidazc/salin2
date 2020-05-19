from django.contrib import admin
from .models import Hero
from .models import Translation

# Register your models here.
admin.site.register(Hero)
admin.site.register(Translation)
