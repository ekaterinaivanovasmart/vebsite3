from django.contrib import admin
from . models import Task #импортировали модель Task из models.py

admin.site.register(Task)

