from django.contrib import admin
from .models import Blog,Categories,Tags
# Register your models here.

admin.site.register(Blog)
admin.site.register(Categories)
admin.site.register(Tags)

