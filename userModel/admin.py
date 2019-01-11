from django.contrib import admin
from .models import Clinic, Hospital,BloodBank, Diagnostics

# Register your models here.


admin.site.register(Clinic)

admin.site.register(Hospital)

admin.site.register(BloodBank)

admin.site.register(Diagnostics)
