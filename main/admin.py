from django.contrib import admin
from .models import Photo, Product, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Photo)