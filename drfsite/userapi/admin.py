from django.contrib import admin

# Register your models here.
from userapi.models import *

admin.site.register(Patient)
admin.site.register(Doctor)
