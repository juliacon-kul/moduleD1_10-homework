from django.contrib import admin
from app.models import Auto

# Register your models here.
@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass

