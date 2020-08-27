from django.contrib import admin
from .models import Blog,Categories,Tags,Comments
# Register your models here.

admin.site.register(Blog)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Comments)

