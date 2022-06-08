from django.contrib import admin
from .models import Address, Bio, Doctor, People, Product

# Register your models here.
admin.site.register(People)
admin.site.register(Address)
admin.site.register(Bio)
admin.site.register(Product)
admin.site.register(Doctor)
