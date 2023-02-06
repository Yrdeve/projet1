from django.contrib import admin
from .models import produit

# Register your models here.
@admin.register(produit)
class ProductAdminAdmin(admin.ModelAdmin):
  list_display = ['nom', 'prix', 'type','datee']

# Register your models here.
