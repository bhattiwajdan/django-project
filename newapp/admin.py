from django.contrib import admin
from newapp.models import ExampleModel

class ExampleAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at')

admin.site.register(ExampleModel,ExampleAdmin)

# Register your models here.
