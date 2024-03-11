from django.contrib import admin
from .models import Registrations
from .models import CustomersComplain
# admin.site.register()
admin.site.register(CustomersComplain)
admin.site.register(Registrations)