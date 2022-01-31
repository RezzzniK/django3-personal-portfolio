from django.contrib import admin

#importing our model from models.py
from .models import Project

#adding the model insed the admin site
admin.site.register(Project)
