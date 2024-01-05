from django.contrib import admin
from myapp.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')


admin.site.register(Person,PersonAdmin)
# Register your models here.
