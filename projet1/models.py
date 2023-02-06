from django.db import models
class produit(models.Model):
    nom = models.CharField(max_length=255)
    datee =models.DateField(auto_now=True)
    prix =models.IntegerField()
    type=models.CharField(max_length=255)

# Create your models here.
