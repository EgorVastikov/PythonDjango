from django.contrib import admin
from .models import Note
from .models import Human

admin.site.register(Note)
admin.site.register(Human)
# Register your models here.
