from django.contrib import admin
from .models import Driver, Rota, MondayThursday, Friday, Saturday, Sunday, DoorCodes

# Register your models here.

admin.site.register(Driver)
admin.site.register(Rota)
admin.site.register(MondayThursday)
admin.site.register(Friday)
admin.site.register(Saturday)
admin.site.register(Sunday)
admin.site.register(DoorCodes)
