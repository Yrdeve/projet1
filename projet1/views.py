from django.shortcuts import render

from .models import produit
from .serializers import ProduitSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class ProduitList(ListAPIView):
  queryset = produit.objects.all()
  serializer_class = ProduitSerializer
