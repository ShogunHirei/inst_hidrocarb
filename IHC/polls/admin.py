from django.contrib import admin

# Polls models
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)

admin.site.register(Choice)

