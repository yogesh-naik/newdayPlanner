from django.contrib import admin
from .models import Task,Comment
# Register your models here.

admin.site.register(Task) # this line will add the model to the admin panel
admin.site.register(Comment) 