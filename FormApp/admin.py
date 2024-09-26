from django.contrib import admin

# Register your models here.
from .models import Student,Profile

class studentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'roll','email','department')

admin.site.register(Student,studentAdmin)
admin.site.register(Profile)